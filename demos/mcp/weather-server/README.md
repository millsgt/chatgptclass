# Weather MCP Server Demo

A minimal Model Context Protocol (MCP) server that provides mock weather information for teaching and demonstration purposes.

## What is MCP?

MCP (Model Context Protocol) allows AI assistants like Claude and GitHub Copilot to interact with external tools and services through a standardized protocol. This weather server demonstrates how to build a simple MCP server with the modern high-level SDK API.

## Available Tools

1. **get_weather** - Get current weather for a specific city
   - Input: `city` (string) - The city name
   - Returns: Temperature, conditions, humidity, wind, and forecast

2. **list_cities** - List all available cities
   - No input required
   - Returns: List of cities with available weather data

## Setup Instructions

1. Install dependencies:
   ```bash
   cd demos/mcp/weather-server
   npm install
   ```
   This installs `@modelcontextprotocol/sdk` (v1.29.0) and `zod`.

2. Run the server directly to confirm it starts:
   ```bash
   node server.js
   ```
   You should see `Weather MCP server running on stdio` on stderr. Press Ctrl+C to stop.

3. Inspect the tools interactively with the MCP Inspector:
   ```bash
   npx @modelcontextprotocol/inspector node server.js
   ```

4. Wire it into VS Code. The server is registered in `.vscode/mcp.json` as the `weather` stdio server and will be available in agent mode after a reload.

## How It Works

The server:
- Uses the modern `McpServer` class from the MCP SDK, which communicates via stdio
- Registers two tools with `server.registerTool(name, { description, inputSchema }, handler)`
- Defines each tool's inputSchema with `zod` validators, so arguments are validated before the handler runs
- Returns mock weather data for demonstration (no API key needed)

## Teaching Points

1. **Modern SDK API** - Uses `McpServer` + `registerTool`, not the deprecated low-level `Server` + `setRequestHandler` pattern
2. **No External Dependencies** - Uses hardcoded data for reliability in demos
3. **Clear Tool Design** - Demonstrates good tool naming, descriptions, and zod input schemas
4. **Graceful Handling** - Shows how to handle unknown cities without throwing

## Example Usage in Claude or Copilot

Once configured, you can ask the agent:
- "What's the weather in Seattle?"
- "Show me all available cities"
- "Compare weather between New York and Miami"
