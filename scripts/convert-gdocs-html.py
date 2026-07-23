#!/usr/bin/env python3
"""Convert a Google Docs HTML export to site MDX."""

from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag


def strip_pua(text: str) -> str:
    return re.sub(r"[\ue000-\uf8ff]", "", text)


def clean_url(href: str) -> str:
    if not href:
        return href
    if "google.com/url" in href:
        parsed = urlparse(href)
        q = parse_qs(parsed.query).get("q", [""])[0]
        return unquote(q) if q else href
    return href


def classes(el: Tag) -> list[str]:
    return el.get("class", [])


def is_bold_span(el: Tag) -> bool:
    cls = classes(el)
    return "c1" in cls or "c11" in cls or ("c9" in cls and "c45" in cls and "c1" in cls)


def inline_md(node: NavigableString | Tag, in_link: bool = False) -> str:
    if isinstance(node, NavigableString):
        return strip_pua(unescape(str(node)))
    if not isinstance(node, Tag):
        return ""

    if node.name == "a":
        href = clean_url(node.get("href", ""))
        text = "".join(inline_md(c, in_link=True) for c in node.children).strip()
        if not text:
            return ""
        return f"[{text}]({href})" if href else text

    if node.name == "br":
        return " "

    if node.name == "span":
        cls = classes(node)
        inner = "".join(inline_md(c, in_link) for c in node.children)
        child_tags = [c for c in node.children if isinstance(c, Tag)]
        if len(child_tags) == 1 and child_tags[0].name == "a":
            return inner
        if not in_link and is_bold_span(node):
            stripped = inner.strip()
            return f"**{stripped}**" if stripped else ""
        if "c5" in cls or "c0" in cls or ("c9" in cls and "c5" in cls):
            stripped = inner.strip()
            return f"`{stripped}`" if stripped else ""
        return inner

    if node.name in ("b", "strong") and not in_link:
        inner = "".join(inline_md(c, in_link) for c in node.children).strip()
        return f"**{inner}**" if inner else ""

    return "".join(inline_md(c, in_link) for c in node.children)


def normalize(text: str) -> str:
    text = strip_pua(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def block_md(el: NavigableString | Tag) -> str:
    if isinstance(el, NavigableString):
        return ""
    if not isinstance(el, Tag):
        return ""
    if el.name in ("script", "style"):
        return ""

    if el.name == "h2":
        text = normalize("".join(inline_md(c) for c in el.children))
        return f"## {text}\n\n" if text else ""

    if el.name == "h3":
        text = normalize("".join(inline_md(c) for c in el.children))
        return f"### {text}\n\n" if text else ""

    if el.name == "table":
        rows = []
        for tr in el.find_all("tr", recursive=False):
            cells = []
            for td in tr.find_all(["td", "th"], recursive=False):
                cell = normalize(
                    " ".join(
                        normalize("".join(inline_md(c) for c in p.children))
                        for p in td.find_all("p")
                    )
                )
                cells.append(cell)
            if any(cells):
                rows.append(cells)
        if not rows:
            return ""
        lines = [
            "| " + " | ".join(rows[0]) + " |",
            "| " + " | ".join(["---"] * len(rows[0])) + " |",
        ]
        for row in rows[1:]:
            row = row + [""] * (len(rows[0]) - len(row))
            lines.append("| " + " | ".join(row[: len(rows[0])]) + " |")
        return "\n".join(lines) + "\n\n"

    if el.name in ("ol", "ul"):
        items = []
        ordered = el.name == "ol"
        for i, li in enumerate(el.find_all("li", recursive=False), 1):
            text = normalize("".join(inline_md(c) for c in li.children))
            prefix = f"{i}." if ordered else "-"
            items.append(f"{prefix} {text}")
        return "\n".join(items) + "\n\n" if items else ""

    if el.name == "p":
        cls = classes(el)
        if "title" in cls:
            return ""
        text = normalize("".join(inline_md(c) for c in el.children))
        if not text:
            return ""
        if "Fionn Gavin" in text and "min read" in text:
            return ""
        if "c6" in cls and "c8" in cls and "introduction to classical" in text.lower():
            return f"_{text}_\n\n"
        return f"{text}\n\n"

    if el.name == "hr":
        return "---\n\n"

    return "".join(block_md(child) for child in el.children)


def post_process(content: str) -> str:
    content = re.sub(
        r"\*\*\s{0,3}([^*\n]{1,120}?)\s{0,3}\*\*",
        lambda match: f"**{match.group(1).strip()}**",
        content,
    )
    content = re.sub(r"\*\*\[([^\]]+)\]\(([^)]+)\)\*\*", r"[\1](\2)", content)
    content = re.sub(r"\)\[", r"), [", content)
    content = re.sub(r"(?<=[a-zA-Z0-9])(\[)", r" \1", content)
    content = re.sub(r"(?<=[a-zA-Z0-9])(\*\*[A-Za-z])", r" \1", content)
    content = re.sub(r"(\*\*[^*\n]{1,120}?\*\*)([a-zA-Z(])", r"\1 \2", content)

    lines = content.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("`") and stripped.endswith("`") and stripped.count("`") == 2:
            code_lines: list[str] = []
            while i < len(lines):
                s = lines[i].strip()
                if not s:
                    if code_lines:
                        i += 1
                        break
                    i += 1
                    continue
                if s.startswith("`") and s.endswith("`") and s.count("`") == 2:
                    code_lines.append(s[1:-1])
                    i += 1
                else:
                    break
            if len(code_lines) >= 2:
                out.extend(["```", *code_lines, "```", ""])
            elif len(code_lines) == 1:
                out.append(f"`{code_lines[0]}`")
                out.append("")
            continue
        out.append(lines[i])
        i += 1

    content = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", content.strip())


def convert(html_path: Path, mdx_path: Path, frontmatter: str) -> None:
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    if not soup.body:
        raise ValueError("HTML file has no body")

    content = post_process(block_md(soup.body))
    mdx_path.parent.mkdir(parents=True, exist_ok=True)
    mdx_path.write_text(frontmatter + content + "\n", encoding="utf-8")


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    fm = sys.argv[3] if len(sys.argv) > 3 else ""
    convert(src, dst, fm)
