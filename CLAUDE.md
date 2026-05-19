# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a ChatGPT and GitHub Copilot training course repository for a 4-hour O'Reilly hands-on workshop (May 2026 delivery). The course teaches professionals how to use AI tools across developer, IT ops, data science, and information worker roles.

## Course Architecture

The repository follows a **4-hour teaching cadence**:
- **Hour 1**: ChatGPT fundamentals (tiers, Projects, Tasks, Custom GPTs)
- **Hour 2**: Advanced ChatGPT + agentic AI (Codex, Images 2.0, data analysis, Personal Finance preview)
- **Hour 3**: GitHub Copilot core (tiers, models, chat modes, custom instructions)
- **Hour 4**: Enterprise + agentic coding (MCP, Copilot CLI, coding agent, governance)

The current course plan lives at `course-plan-may-2026.md`. A detailed news timeline is at `whats-new-may-2026.md`. Previous plans are archived in `docs/archive/`.

## Key File Relationships

- `course-plan-may-2026.md` - Master course plan with detailed timings and content
- `warner-chatgpt-github-copilot-may-2026.pptx` - Presentation deck (binary, matches course plan)
- `.github/copilot-instructions.md` - Teaching example for Copilot custom instructions
- `.github/agents/` - Custom agent definitions (teaching examples)
- `.github/instructions/` - Path-specific instruction files (teaching examples)
- `docs/instructor/mcp-teaching.guide.md` - MCP demo setup with 3 Python servers (calculator, weather, docs-generator)

## Running Demo Code

**OpenAI API examples:**
```bash
export OPENAI_API_KEY="your-key"
python demos/chatgpt/api-examples/call_openai_api.py
```

**MCP demo servers** (require `pip install "mcp[cli]" httpx`):
```bash
# Calculator server
python demos/mcp/calculator-mcp.py

# Weather server (from teaching guide)
python demos/mcp/weather-mcp.py

# MCP Inspector for testing
npx @modelcontextprotocol/inspector
```

**Weather MCP server** (Node.js):
```bash
cd demos/mcp/weather-server && npm install && node server.js
```

**Vulnerable demo** (Docker):
```bash
docker build -f demos/vulnerable-code/Dockerfile -t chatgpt-demo .
docker run -p 5000:5000 chatgpt-demo
```

## Intentionally Vulnerable Code

`demos/vulnerable-code/` and `demos/security-scanning/` contain **intentionally insecure** code and outdated dependencies for security education demos. Do not "fix" these unless explicitly asked. The `requirements.txt` in `demos/vulnerable-code/` has known CVEs by design.

## Technology Landscape (May 2026)

When updating course content, these are the current-gen references:

**ChatGPT / OpenAI**: GPT-5.5 Instant (default chat, May 5, 2026; 52.5% fewer hallucinations than 5.3), GPT-5.5 / 5.5 Pro (flagship, April 23-24; xhigh reasoning), GPT-5.4 Thinking / 5.4 Pro (March 5; mainline reasoning, 1M context in API), GPT-5.3-Codex + `codex-1` (coding); Codex apps on macOS / Windows / mobile preview; $100 ChatGPT Pro tier (April 9); ChatGPT Images 2.0 (April 21, text-in-image); Memory Sources (May, all plans); Personal Finance preview (US Pro, May 15, via Plaid); Codex browser verification (April); Tasks (Plus 40/mo, Pro unlimited); ChatGPT Agent (browser automation via /agent); Deep Research (GPT-5.5 powered); Canvas (out of beta). **Sora 2 discontinued globally April 26, 2026.** GPT-4o/4.1/o4-mini retired Feb 13. GPT-5.3 Instant retiring ~August 2026.

**GitHub Copilot**: VS Code v1.116-v1.119 (April-May 2026) shipped agent debug logs, BYOK for Business/Enterprise (v1.117), semantic codebase search + grep across orgs (v1.118), `/chronicle` chat-history queries (v1.119), agent terminal read/write, remote control of CLI sessions from github.com/mobile, agent inline diffs, browser tab sharing. Copilot CLI (GA Feb 25; current **v1.0.48** as of May 14, 2026) with plan/autopilot/remote modes; coding agent with **Claude Sonnet 4.8** default (mid-May); models include **Claude Opus 4.7** (1M context, 3x image res, xhigh effort), GPT-5.3-Codex, Gemini 3 Pro/Flash. **Grok Code Fast 1 deprecated May 15, 2026.** Visual Studio April update (April 30): cloud agents from IDE, user-level custom agents, **Debugger agent** validates fixes against live runtime. Enterprise AI Controls GA (Feb 26); Copilot SDK (tech preview); Copilot Memory on by default for Pro/Pro+; Mission Control + Agents tab in every repo.

**MCP**: Donated to Agentic AI Foundation (Linux Foundation) Dec 2025; **2,000+ servers**; Nov 2025 spec with async Tasks, OAuth 2.1, statelessness; **MCP Apps (SEP-1865)** formalized April 2026 -- interactive UIs from servers via `ui://` scheme, sandboxed iframes, bi-directional JSON-RPC, co-developed by Anthropic + OpenAI; Azure MCP Server preview; MCP Dev Summit NYC Apr 2-3, 2026 (~1,200 attendees).

**Claude / Anthropic**: Opus 4.7 (April 16, 2026; 3x image resolution, vision verification, xhigh effort level, literal instruction following), Sonnet 4.8 (~mid-May 2026; new mid-tier default), Claude Code 2.x (skills, auto-memory, /teleport, custom agents, hooks, wildcard tool permissions).
