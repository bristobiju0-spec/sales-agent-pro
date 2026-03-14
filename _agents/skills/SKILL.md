---
name: Lead Generation Agent
description: A mock LinkedIn research tool to gather prospect information.
---

# Lead Generation Agent Skill

This skill allows the agent to use the Lead Generation MCP Server to perform mocked searches for prospect data (like LinkedIn profiles).

## How to use

1. Install the requirements first: `pip install -r /home/bristo/sales-agent-pro/requirements.txt`
2. Start the server: `python /home/bristo/sales-agent-pro/mcp_server.py`
3. Connect to the MCP server.

### Available Tools

- `research_prospect`: Tool to search for a prospect's information.
    - Requires `name` (string)
    - Optional `company` (string)
    
It returns a summary string of the prospect, focusing on contact probability and recent activity.
