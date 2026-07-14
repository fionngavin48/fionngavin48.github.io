---
title: "IBM MCP Server Vulnerability Scanner"
summary: "Security validation for a Model Context Protocol gateway and registry — multi-protocol transport and production-grade deployment. Built with IBM for a second-year software engineering project."
type: "security"
year: 2026
tags: ["python", "fastapi", "security"]
repo: "https://github.com/IBM/mcp-context-forge"
featured: true
writeup: true
order: 1
---

## What it is

[IBM's MCP Context Forge](https://github.com/IBM/mcp-context-forge) is a gateway and registry for the Model Context Protocol — it centralises the tools, resources, and prompts that LLM applications call. I worked on it as my second-year software engineering project, in collaboration with IBM.

My focus was the security layer: making sure anything registered with the gateway can only do what it is allowed to do.

## My role

- _TODO: the specific components you owned (e.g. the scanner module, the auth checks, transport validation)._
- _TODO: team size and how the work was divided._

## How it works

The gateway sits between an LLM client and many downstream MCP servers, so it is the natural place to enforce policy. The checks that matter most are the boring, high-value ones:

- every registered route resolves to an explicit permission
- transport input is validated before it reaches a handler
- _TODO: add the concrete checks you implemented._

## What I took away

Security work is mostly bookkeeping, done well. The interesting bugs lived on paths that no single person owned. _TODO: one specific thing that surprised you._
