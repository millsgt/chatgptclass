# MCP Server Demo Guide

## Quick Setup

1. **Install the weather server dependencies:**
   ```bash
   cd demos/mcp/weather-server
   npm install
   ```
   This pulls in `@modelcontextprotocol/sdk` (v1.29.0) and `zod`.

2. **Confirm the server starts:**
   ```bash
   node server.js
   ```
   Look for `Weather MCP server running on stdio` on stderr, then Ctrl+C to stop.

3. **Inspect the tools with the MCP Inspector (optional):**
   ```bash
   npx @modelcontextprotocol/inspector node server.js
   ```

4. **Reload VS Code** to load the MCP configuration from `.vscode/mcp.json` (the `weather` stdio server)

5. **In agent mode (Claude or Copilot)**, you can now use weather commands!

## Demo Script

### Basic Weather Query
"What's the weather in Seattle?"

### List Available Cities
"What cities do you have weather data for?"

### Compare Weather
"Compare the weather between Miami and Chicago"

### Error Handling Demo
"What's the weather in Paris?" (Shows graceful error handling)

## How MCP Works

1. **Configuration**: `.vscode/mcp.json` tells VS Code which MCP servers to run
2. **Server**: The Node.js server uses the modern `McpServer` class from the MCP SDK and registers tools with `server.registerTool`
3. **Tools**: Each tool declares a `zod` inputSchema, so arguments are validated before the handler runs
4. **Integration**: The agent automatically discovers and calls these tools over stdio

## Teaching Points

- **Extensibility**: Show how easy it is to add new cities or weather properties
- **Protocol**: Explain the request/response pattern
- **Real-world Use**: Discuss how this could connect to real weather APIs
- **Error Handling**: Demonstrate robustness with invalid inputs

## Troubleshooting

- If tools don't appear, reload VS Code
- Check the Output panel (View > Output > "MCP") for server logs
- Ensure Node.js is installed (`node --version`)
- If the server fails to start, re-run `npm install` in `demos/mcp/weather-server` to fetch `@modelcontextprotocol/sdk` and `zod`

## Next Steps

1. Try enabling the filesystem MCP server (set `"disabled": false`)
2. Add more weather properties (UV index, precipitation, etc.)
3. Create your own MCP server for a different domain!