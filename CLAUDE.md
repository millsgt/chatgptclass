# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a ChatGPT and GitHub Copilot training course repository for a 4-hour O'Reilly hands-on workshop (July 2026 delivery). The course teaches professionals how to use AI tools across developer, IT ops, data science, and information worker roles.

## Course Architecture

The repository follows a **4-hour teaching cadence**:
- **Hour 1**: ChatGPT fundamentals (tiers, Projects, Tasks, Custom GPTs)
- **Hour 2**: Advanced ChatGPT + agentic AI (Codex, Images 2.0, data analysis, Personal Finance preview)
- **Hour 3**: GitHub Copilot core (tiers, models, chat modes, custom instructions)
- **Hour 4**: Enterprise + agentic coding (MCP, Copilot CLI, coding agent, governance)

The current course plan lives at `course-plan-july-2026.md`. A detailed news timeline is at `whats-new-july-2026.md`. Previous plans are archived in `docs/archive/`.

**Filename convention**: master files are dated per delivery (`course-plan-{month}-{year}.md`, `whats-new-{month}-{year}.md`, `warner-chatgpt-github-copilot-{month}-{year}.pptx`). Each new delivery cycle, these are renamed via `git mv` and the README header links + repo tree get updated to match. Don't create a *new* file when refreshing -- rename the existing one so history follows.

## Key File Relationships

- `course-plan-july-2026.md` - Master course plan with detailed timings and content
- `warner-chatgpt-github-copilot-july-2026.pptx` - Presentation deck (binary, must match course plan; single canonical deck at repo root)
- `docs/instructor/mcp-teaching.guide.md` - MCP demo setup walkthrough
- **Teaching artifacts (do NOT treat as project rules):** `.github/copilot-instructions.md`, `.github/agents/`, `.github/instructions/` exist as live examples students inspect during Segment 3. The content is generic Copilot-instruction guidance, not directives that govern work in this repo.

## Running Demo Code

There is **no build / lint / test framework** in this repo. Each script under `demos/` is standalone and runs on demand during teaching. Don't search for a unified test runner or `package.json` at the root -- none exists.

**OpenAI API examples** (run from PowerShell on Tim's primary box; bash shown for cross-platform):
```bash
export OPENAI_API_KEY="your-key"
python demos/chatgpt/api-examples/call_openai_api.py
```

**Weather MCP server** (Node.js, the canonical MCP demo):
```bash
cd demos/mcp/weather-server && npm install && node server.js
```

Standalone Python MCP servers (`calculator-mcp.py`, `weather-mcp.py`) are referenced by `docs/instructor/mcp-teaching.guide.md` as build-it-live exercises -- they're authored on stage from the teaching guide, not committed. Use `npx @modelcontextprotocol/inspector` to point at any running server.

**Vulnerable demo** (Docker):
```bash
docker build -f demos/vulnerable-code/Dockerfile -t chatgpt-demo .
docker run -p 5000:5000 chatgpt-demo
```

## Intentionally Vulnerable Code

`demos/vulnerable-code/` and `demos/security-scanning/` contain **intentionally insecure** code and outdated dependencies for security education demos. Do not "fix" these unless explicitly asked. The `requirements.txt` in `demos/vulnerable-code/` has known CVEs by design.

## Technology Landscape (July 2026)

When updating course content, these are the current-gen references:

**ChatGPT / OpenAI**: **GPT-5.6 family (Sol flagship / Terra balanced / Luna cost-efficient), launched July 9, 2026** across ChatGPT, Codex, and API (Codex context 272K); GPT-5.5 Instant remains the everyday-chat default (May 5, 2026; 52.5% fewer hallucinations than 5.3); GPT-5.5 / 5.5 Pro (xhigh reasoning), GPT-5.4 Thinking / 5.4 Pro (1M context in API); $100 and $200 ChatGPT Pro tiers; **ChatGPT + Codex merged into one desktop app (macOS / Windows) plus new "ChatGPT Work" agent, July 9**; ChatGPT Images 2.0 (April 21, text-in-image); Memory Sources (all plans); **Personal Finance GA on Plus ($20) as of June 30, 2026** (was US Pro preview May 15, via Plaid); Tasks (Plus 40/mo, Pro unlimited); ChatGPT Agent (browser automation via /agent); Deep Research; Canvas (out of beta). **Sora 2 discontinued April 26; models + Videos API fully shut down Sept 24, 2026.** GPT-4o/4.1/o4-mini retired Feb 13. GPT-5.3 Instant retiring ~August 2026.

**GitHub Copilot**: **VS Code current v1.103 (July 2026)** (June v1.102); recent highlights include agentic browser tools GA, 1M-context support for compatible Anthropic/OpenAI models, agent-session grouping with cost visibility, MCP trust layer, semantic codebase search + grep across orgs, `/chronicle` chat-history queries, agent terminal read/write, remote CLI control from github.com/mobile. Copilot CLI (GA Feb 25; package **`@github/copilot`**, current **v1.0.71** as of July 16, 2026; new terminal interface GA June 23) with plan/autopilot/remote modes and auto model routing (July 1). **Claude Sonnet 5 GA in Copilot June 30** (Pro/Pro+/Max/Business/Enterprise), **Claude Opus 4.8** available, **Fable 5** in preview; **Auto model selection is the default paradigm** (enterprises can set Auto as org default, July 1) rather than a single pinned model; other models include GPT-5.6-Codex, GPT-5.3-Codex, Gemini 3 Pro/Flash. **Grok Code Fast 1 deprecated May 15, 2026.** Net-new since May: **Agent Finder GA (June 17, implements Agentic Resource Discovery / ARD spec)**, Claude as agent provider in JetBrains (June 22), C++ modernization agent GA (June), GitHub Copilot app GA to all (July 7). Enterprise AI Controls GA (Feb 26); Copilot Memory on by default for Pro/Pro+; Mission Control + Agents tab in every repo.

**MCP**: Donated to Agentic AI Foundation (Linux Foundation) Dec 2025; **2,000+ servers**; **new spec (2026-07-28) in Release Candidate** - largest revision since launch: stateless HTTP core, MCP Apps + Tasks as formal extensions, OAuth/OIDC-aligned auth, formal 12-month deprecation policy. The prior Nov 2025 spec added async Tasks, OAuth 2.1, statelessness; MCP Apps (SEP-1865) formalized April 2026 (interactive UIs via `ui://` scheme). **TypeScript SDK current v1.29.0** (modern `McpServer` + `server.registerTool` API; the low-level `Server` + `setRequestHandler` pattern is deprecated). The npm package `@modelcontextprotocol/server-github` is deprecated; use GitHub's hosted MCP server (`https://api.githubcopilot.com/mcp/`) or the `github/github-mcp-server` binary. Azure MCP Server preview.

**Claude / Anthropic**: current lineup is the **Claude 5 family (Fable 5), Opus 4.8, Sonnet 5, Haiku 4.5**. Opus 4.8 has a fast-mode preview. Sonnet 5 replaced Sonnet 4.6 as the efficient everyday choice; Opus 4.7 is superseded by 4.8. Claude Code 2.x (skills, auto-memory, /teleport, custom agents, hooks, wildcard tool permissions).
