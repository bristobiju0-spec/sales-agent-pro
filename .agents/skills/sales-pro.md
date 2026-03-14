---
name: "Marketplace-Ready Sales Prospector"
description: "MCP-powered tool for researching LinkedIn prospects and generating personalized outreach."
version: "1.0.0"
category: "Sales Operations"
author: "Bristo"
---

# Instructions for the AI Agent
When a user provides a name or company, use the `research_prospect` tool to fetch data.
1. Analyze the 'Recent News' or 'Bio' returned by the tool.
2. Draft a 3-sentence outreach email that mentions a specific fact found in the research.
3. If the tool returns 'Data not found', ask the user for a direct LinkedIn URL.

# Safety & Compliance
- Never store prospect data in the global memory file.
- Do not scrape more than 5 profiles per session to avoid API rate limits.
