// Minimal Model Context Protocol (MCP) server for the O'Reilly ChatGPT + GitHub Copilot course.
//
// This is the canonical MCP demo. It returns MOCK weather data so it always
// works on stage with no API key and no network dependency. It uses the modern
// high-level McpServer API from MCP TypeScript SDK v1.29.0:
//   - McpServer            (server/mcp.js)    high-level server, auto-handles tool discovery
//   - server.registerTool  registers a tool with a zod inputSchema
//   - StdioServerTransport (server/stdio.js)  stdio is how VS Code and the Inspector talk to us
//
// Run it live:  npm install && node server.js
// Inspect it:   npx @modelcontextprotocol/inspector node server.js

import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

// Mock weather data keyed by lowercase city name. Hardcoded on purpose so the
// demo is deterministic and reliable in front of a live audience.
const WEATHER_DATA = {
  'seattle': {
    temp: 55,
    condition: 'Rainy',
    humidity: 85,
    wind: '10 mph SW',
    forecast: 'Rain continuing throughout the week'
  },
  'los angeles': {
    temp: 75,
    condition: 'Sunny',
    humidity: 40,
    wind: '5 mph W',
    forecast: 'Clear skies for the next 5 days'
  },
  'new york': {
    temp: 62,
    condition: 'Partly Cloudy',
    humidity: 60,
    wind: '15 mph NE',
    forecast: 'Scattered clouds, possible rain tomorrow'
  },
  'miami': {
    temp: 82,
    condition: 'Humid',
    humidity: 75,
    wind: '8 mph E',
    forecast: 'Hot and humid with afternoon thunderstorms'
  },
  'chicago': {
    temp: 48,
    condition: 'Windy',
    humidity: 55,
    wind: '20 mph NW',
    forecast: 'Cold front moving in, temperatures dropping'
  },
  'denver': {
    temp: 45,
    condition: 'Clear',
    humidity: 30,
    wind: '12 mph W',
    forecast: 'Clear and cold, possible snow in mountains'
  }
};

// The high-level server. name and version show up in the MCP handshake so
// clients (VS Code, the Inspector) can identify us.
const server = new McpServer({
  name: 'weather-server',
  version: '1.0.0'
});

// get_weather: the headline tool. The inputSchema is a plain object of zod
// validators, which the SDK converts to a JSON Schema for the client AND uses
// to validate incoming arguments before our handler runs, so args.city is
// always a present string by the time we see it.
server.registerTool(
  'get_weather',
  {
    description: 'Get current weather for a city',
    inputSchema: {
      city: z.string().describe('The city name, for example "Seattle" or "New York"')
    }
  },
  async ({ city }) => {
    const key = city.toLowerCase();
    const weather = WEATHER_DATA[key];

    // Graceful miss: return a helpful message instead of throwing, so the
    // "What is the weather in Paris?" demo shows sane behavior on unknown cities.
    if (!weather) {
      return {
        content: [
          {
            type: 'text',
            text: `Weather data not available for "${city}". Available cities: ${Object.keys(WEATHER_DATA).join(', ')}`
          }
        ]
      };
    }

    return {
      content: [
        {
          type: 'text',
          text: `Weather in ${city}:
Temperature: ${weather.temp}F
Condition: ${weather.condition}
Humidity: ${weather.humidity}%
Wind: ${weather.wind}
Forecast: ${weather.forecast}`
        }
      ]
    };
  }
);

// list_cities: a zero-argument tool. An empty inputSchema object tells the SDK
// this tool takes no parameters.
server.registerTool(
  'list_cities',
  {
    description: 'List all available cities with weather data',
    inputSchema: {}
  },
  async () => {
    const cities = Object.keys(WEATHER_DATA)
      .map((city) => city.charAt(0).toUpperCase() + city.slice(1))
      .join(', ');

    return {
      content: [
        {
          type: 'text',
          text: `Available cities with weather data: ${cities}`
        }
      ]
    };
  }
);

// Connect over stdio and start serving. We log to stderr because stdout is the
// JSON-RPC channel, so anything printed to stdout would corrupt the protocol.
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Weather MCP server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error starting weather MCP server:', error);
  process.exit(1);
});
