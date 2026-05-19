# ChatGPT + GitHub Copilot in 4 Hours -- May 2026

> Presenter run sheet. Each segment is ~50 minutes with a 10-minute break between.

---

## At a Glance

| Segment | Name | What You Cover |
|---------|------|----------------|
| **1** | **ChatGPT Power User** | Tiers, Projects, Tasks, Canvas, Custom GPTs, ChatGPT Agent |
| **2** | **ChatGPT for Builders** | Codex, Deep Research, Data Analysis, Images 2.0, Codex CLI |
| **3** | **Copilot in the Editor** | Tiers, models, inline suggestions, Ask/Edit/Agent/Plan modes, custom instructions |
| **4** | **Copilot Beyond the Editor** | MCP, Copilot CLI, coding agent (@copilot), enterprise governance |

---

## Segment 1: ChatGPT Power User (50 min)

### SHOW: Tiers & Models (8 min)

Open chatgpt.com/pricing. Walk through the table live.

| Tier | Price | Highlights |
|------|-------|-----------|
| Free | $0 | GPT-5.5 Instant, 2 images/day, basic memory, inline web images, ads in US |
| Go | $8/mo | 10x messages, file uploads, custom GPTs, File library, longer memory |
| Plus | $20/mo | GPT-5.5, GPT-5.5 Thinking, Deep Research 25/mo, Tasks 40/mo, Advanced Voice |
| **Pro (new tier)** | **$100/mo** | **5x Codex vs Plus, unlimited GPT-5.5 Instant + Thinking, GPT-5.5 Pro** |
| Pro Max | $200/mo | Everything in Pro + 10x Codex, o3-pro, 2M context, Pulse, Personal Finance preview (US) |
| Team | $25-30/user | Admin controls, shared workspaces |
| Enterprise | Custom | SSO/SCIM, data controls, Frontier platform |

Quick model overview -- show the model picker dropdown:
- **GPT-5.5 Instant** = new default (May 5, 2026); 52.5% fewer hallucinations vs 5.3 on legal/medical/finance, same low latency
- **GPT-5.5 / 5.5 Pro** = flagship; xhigh reasoning mode; API $5/$30 (5.5), $30/$180 (5.5-pro)
- **GPT-5.4 Thinking / 5.4 Pro** = mainline reasoning, 1M context window in API
- **GPT-5.3-Codex / 5.3-Codex-Spark** = coding workhorse (Codex CLI default is `codex-1`)
- **Retired Feb 13:** GPT-4o, GPT-4.1, o4-mini. **Retiring ~August 2026:** GPT-5.3 Instant

### SHOW: Canvas (5 min)

Open a Canvas session. Show:
1. Two-pane editing (conversation + document)
2. Writing mode: suggest edits, adjust reading level
3. Coding mode: review code, add comments, port languages
4. Export to Word/PDF/Markdown

> Canvas is out of beta. Compliance API available for admins.

### SHOW: Projects (10 min)

Create a new Project live:
1. Name it "Product Launch"
2. Upload a marketing brief PDF and budget spreadsheet
3. Add custom instructions: "You are a product marketing manager. Be concise."
4. Start a chat inside the project -- show it uses the uploaded files
5. Show "Branch in new chat" to split a conversation

> Projects available to ALL tiers including Free. Connect Google Drive / OneDrive.
>
> **Memory Sources** (May 2026, all plans): every response now shows what context shaped it -- saved memories, past chats, files. Delete specific sources without wiping history.

### SHOW: Tasks (5 min)

In the same Project:
1. Type: "Every Monday at 8am, summarize my project files and email me the highlights"
2. Show the Tasks panel (chatgpt.com/schedules)
3. Show schedule options: daily, weekly, monthly
4. Mention Pulse dashboard (Pro only)

> Plus: 40 tasks/mo. Pro: unlimited. Up to 10 active. Web/iOS/Android/macOS only.

### SHOW: Custom GPTs + ChatGPT Agent (12 min)

**Build a GPT** (8 min):
1. Go to chatgpt.com/create
2. Name: "HR Assistant"
3. Upload `datasets/Human Resources/HRIS.csv` as knowledge
4. Enable Code Interpreter + Web Search
5. Test: "What's the average salary by department?"
6. Mention GPT Store (3M+ GPTs) and Builder Profile verification

**ChatGPT Agent** (4 min):
1. Type `/agent` in any chat
2. Show browser automation -- "Go to weather.com and get the forecast for Nashville"
3. Mention: 100+ MCP app connections, available Plus/Pro/Team/Enterprise/Edu
4. **Codex mobile app preview** (May 2026): stay connected to running Codex tasks from phone while work continues on a connected Mac

### LAB 1 (10 min)

Students do:
1. Create a Project, upload `datasets/Human Resources/HRIS.csv`, add HR custom instructions
2. Build an "HR Assistant" GPT with Code Interpreter
3. Query: "Show a bar chart of headcount by department"
4. Bonus: Create a weekly Task for a Monday morning HR digest

---

## Segment 2: ChatGPT for Builders (50 min)

### SHOW: OpenAI Codex (15 min)

**Demo the cloud agent:**
1. Open chatgpt.com/codex
2. Show an existing completed task (PR merged)
3. Assign a GitHub issue live -- walk through the async flow
4. While it works, explain:
   - Powered by **GPT-5.3-Codex** (still the workhorse, 25% faster than 5.2-Codex)
   - **codex-1** is the Codex CLI default for low-latency edits
   - **GPT-5.3-Codex-Spark** for real-time coding (1000+ tokens/sec)
   - 352K+ PRs merged at 85% success rate
   - Runs in isolated cloud sandboxes
   - **Browser verification** (April 2026): Codex can drive the in-app browser to verify visual fixes on local servers

**Access points**: chatgpt.com/codex | CLI | VS Code/Cursor/Windsurf | @codex in GitHub comments

**Codex apps**: **macOS** (Feb 2), **Windows** (Mar 3), **mobile preview** (May 2026). Parallel agents, isolated worktrees, reviewable diffs.

### SHOW: Deep Research (8 min)

1. Start a Deep Research query: "Compare the top 3 MCP server frameworks for Python"
2. Show the **research plan** -- edit it before execution
3. Show **site restriction**: limit to specific trusted sources
4. Show **real-time steering**: interrupt and refine mid-research
5. When done, show **fullscreen document viewer** and export to Word

> Powered by GPT-5.5. Plus: 25/mo. Pro: 250/mo. MCP integration available.

### SHOW: Data Analysis (7 min)

1. Upload `datasets/Financial/sales_data.csv`
2. Prompt: "Create 3 charts showing revenue trends by quarter, top products, and regional breakdown. Then export to PowerPoint."
3. Show the generated charts (interactive + static)
4. Download the PowerPoint

> Runs Python (pandas, matplotlib, plotly) in sandbox. Handles CSV/XLSX/JSON up to 512MB.
>
> **Personal Finance preview** (Pro/US, May 15, 2026): connects via Plaid to 12,000+ financial institutions (Schwab, Fidelity, Chase, Robinhood, Amex, Capital One). Money dashboard, grounded finance Q&A, Financial memories for savings goals / mortgages / planned purchases. Show the dashboard if instructor has US Pro account.

### SHOW: ChatGPT Images 2.0 + Inline Web Images (5 min)

Sora 2 was discontinued globally **April 26, 2026**. The slot it used to fill now goes to the new image stack.

1. **Images 2.0** (April 21, 2026): generate an image with on-image **text rendering** -- the long-standing weakness of diffusion models, finally usable. Prompt: "a 1970s sci-fi paperback cover with the title 'AGENT HQ' in bold serif text."
2. **Free-tier inline images** (May 2026): when you ask about a person, place, or product, ChatGPT now embeds web images directly in the chat. Show with "What does the new Codex Windows app icon look like?"
3. For video generation, point students at **Veo** (Google) and **Runway**. No first-party OpenAI video product in May 2026.

### SHOW: Codex CLI (5 min)

Quick terminal demo:
```bash
npm i -g @openai/codex
codex "explain this codebase structure"
```

Show approval modes: Auto (default) | Read Only | Full Access

> Difference from Copilot CLI: Codex CLI = autonomous hours-long tasks. Copilot CLI = interactive terminal agent.

### LAB 2 (10 min)

Students do:
1. Open chatgpt.com/codex and assign a GitHub issue (or watch instructor demo)
2. Upload a CSV, ask for "3 charts + PowerPoint export"
3. If time: run `codex "explain this codebase"` locally

---

## Segment 3: Copilot in the Editor (50 min)

### SHOW: Tiers & Models (5 min)

Open github.com/features/copilot/plans. Walk through live.

| Tier | Price | Premium Requests |
|------|-------|-----------------|
| Free | $0 | 50/mo (2,000 completions) |
| Pro | $10/mo | 300/mo |
| Pro+ | $39/mo | 1,500/mo |
| Business | $19/user/mo | Org-level |
| Enterprise | $39/user/mo | + knowledge bases, custom models |

**Model picker** (show the dropdown in VS Code):
- **Auto-select** = 10% premium request discount (GPT-4.1, GPT-5 mini, Claude Haiku 4.5, etc.)
- **Free models**: GPT-4.1, GPT-5 mini (no premium cost)
- **Premium**: **Claude Opus 4.7** (April 16, 3x image resolution, xhigh effort, vision verification), **Claude Sonnet 4.8** (mid-May, new default for most users), GPT-5.3-Codex, Gemini 3 Pro, o3
- **Deprecated May 15, 2026**: Grok Code Fast 1 removed across Chat, inline edits, ask/agent modes, and completions

### SHOW: Inline Suggestions (10 min)

Open a Python file. Code live and show:

| Action | Shortcut |
|--------|----------|
| Accept suggestion | `Tab` |
| Accept next word only | `Ctrl+Right` |
| Cycle alternatives | `Alt+]` / `Alt+[` |
| Trigger manually | `Alt+\` |
| Open Chat panel | `Ctrl+Alt+I` |
| Inline chat | `Ctrl+I` |

Demo: write a function signature + docstring comment, let Copilot complete the body. Show partial acceptance (word-by-word with Ctrl+Right). Toggle Next Edit Suggestions (NES) from status bar.

### SHOW: Chat Modes (15 min)

Open Copilot Chat. Demonstrate all four modes on the **same task**: "Add input validation to this Express endpoint."

**Ask mode** (2 min): Get an explanation, no files touched.

**Edit mode** (3 min): Select files, get targeted changes, review diff, accept/reject.

**Agent mode** (5 min): Let it autonomously plan, edit files, run terminal commands, self-correct errors. Show Copilot Memory (on by default for Pro/Pro+) learning repo conventions. **Agent terminal R/W** (April 2026): agents read and write to any open terminal, including running REPLs and interactive scripts -- demo with an active Python REPL.

**Plan mode** (3 min): Get a structured implementation plan, review it, then approve to execute.

> Agent mode always consumes premium requests. Edit mode is more predictable.

**Chat participants**: `@workspace`, `@terminal`, `@vscode`
**Variables**: `#codebase`, `#editor`, `#selection`, `#file`, `#git`
**Slash commands**: `/explain`, `/fix`, `/tests`, `/doc`, `/generate`, `/new`, **`/chronicle`** (experimental, queries your chat history)

### SHOW: Semantic Search + /chronicle (5 min)

VS Code v1.118+ (rolled out April-May 2026):

1. **Semantic codebase search**: "find code that handles user authentication" returns matches by **meaning**, not just keywords. Compare to a regular text search to make the difference obvious.
2. **Grep-style queries across GitHub repos and orgs**: search outside the open workspace -- great for "how do we do X in our other repos?"
3. Experimental **`/chronicle`** in chat: "what did I work on last Tuesday?" -- queries your own chat history for files touched, PRs referenced, decisions made. Great standup-prep tool.

### SHOW: Custom Instructions & Agents (10 min)

Walk through the instruction hierarchy:

**1. Repository instructions** -- `.github/copilot-instructions.md`
```markdown
# Project Context
React + TypeScript e-commerce app.
## Coding Standards
- Functional components with hooks
- TypeScript strict mode
```

**2. Path-specific instructions** -- `.github/instructions/*.instructions.md`
```yaml
---
applyTo: "src/components/**/*.tsx"
---
Use React.memo for all components. Prefer composition over inheritance.
```

**3. Custom agents** -- `.github/agents/*.agent.md`
```yaml
---
name: "code-reviewer"
description: "Reviews code for quality and security"
model: "claude-opus-4.6"
tools: ["codebase", "terminal"]
---
Review for OWASP Top 10 vulnerabilities...
```

**4. Reusable prompts** -- `.github/prompts/*.prompt.md`

**5. Organization instructions** (Enterprise only)

### LAB 3 (5 min)

Students do:
1. Try the same prompt ("add input validation") in Ask, Edit, and Agent modes
2. Create a `.github/copilot-instructions.md` in their repo
3. Use `@workspace` + `#selection` for targeted help

---

## Segment 4: Copilot Beyond the Editor (50 min)

### SHOW: MCP - Model Context Protocol (10 min)

**Explain** (3 min):
- "USB-C for AI" -- one standard to connect AI to any tool
- Donated to Linux Foundation's AAIF (Dec 2025) -- co-founded by Anthropic, OpenAI, Block
- **2,000+ servers** in ecosystem. **MCP Dev Summit NYC** (Apr 2-3, 2026) drew ~1,200 attendees
- **Nov 2025 spec** (still current): async Tasks primitive, OAuth 2.1, statelessness by default
- **April 2026: MCP Apps (SEP-1865)** formalized -- servers can deliver interactive React/HTML UIs to ChatGPT and Claude hosts via the `ui://` scheme, sandboxed iframes, bi-directional JSON-RPC

**Demo** (7 min): Show MCP in VS Code
1. Open `.vscode/mcp.json` -- show GitHub MCP server config
2. In Agent mode, ask: "List my open GitHub issues" -- show tool invocation
3. Show MCP Registry in VS Code (one-click install)
4. Mention: Azure MCP Server (Preview), Playwright MCP, Figma MCP

| Server | What It Does |
|--------|-------------|
| GitHub MCP | Issues, PRs, repos, **Spaces tools** |
| Azure MCP | Azure resources via natural language |
| Figma | Design-to-code |
| Playwright | Test generation from DOM |
| Postman | API platform |
| **MCP Apps** | **Interactive UI components (forms, dashboards) rendered inside chat** |

> Enterprise: org-level MCP allowlists, registry-only mode, 30-min propagation.

### SHOW: Copilot CLI (10 min)

**Live terminal demo** (GA Feb 25, 2026; current **v1.0.48** as of May 14, 2026):

```bash
# Install
npm install -g @github/copilot-cli

# Start
copilot
/login
```

Show these modes live:
1. **Interactive**: ask a question, get code + explanation
2. **Plan mode** (`Shift+Tab`): structured plan before coding
3. **Autopilot**: autonomous execution with no approval gates
4. **Shell execution**: `!git log --oneline -5`
5. **Delegation**: `/delegate` hands off to coding agent on GitHub
6. **Remote control** (April 2026): start, steer, and stop CLI sessions from github.com or GitHub Mobile -- handy when you start a long-running task on your desktop and want to monitor from your phone
7. **Token-priced model picker** (v1.0.48): shows actual $/M-token prices instead of dot indicators

Built-in agents: Explore (codebase analysis), Task (builds/tests), Code-review

> Models: **Claude Sonnet 4.8** default (mid-May 2026). GPT-5 mini / GPT-4.1 included free. Built-in GitHub MCP.

### SHOW: Coding Agent (10 min)

**Live demo** -- assign an issue to @copilot:
1. Open a GitHub issue (pre-prepared, something simple like "Add a health check endpoint")
2. Assign to **@copilot**
3. Explain the flow while it works:
   - Boots secure VM, clones repo
   - Analyzes with GitHub code search
   - Creates `copilot/*` branch
   - Writes code, runs tests, self-reviews
   - Opens draft PR with security scanning
4. Show the resulting PR, check the diff
5. Leave a review comment -- show the agent responding

**New in 2026**: model picker, self-review, built-in security scanning, custom agents, code referencing, CLI handoff

**Mission Control** (now lives in the **Agents tab** in every repo): assign across repos, watch real-time session logs, pause/refine/restart mid-run, jump straight into the resulting PRs -- all from one view. Demo it after the issue assignment completes.

> Available: Pro, Pro+, Business, Enterprise. Claude and Codex models for Business/Pro (Feb 26, 2026). Visual Studio **Debugger agent** (April 30, 2026) validates fixes against live runtime behavior.

### SHOW: Enterprise Governance (10 min)

**Enterprise AI Controls & Agent Control Plane** (GA Feb 26, 2026):
1. Show the consolidated AI Controls navigation
2. Show agent audit logging (filter by agent type, last 24h)
3. Show policy management: Feature, Privacy, Models

**Content Exclusion**: pattern-based file exclusion (`*.cfg`, `secrets/**`)
- Configure at enterprise/org/repo level
- NOT supported in CLI, coding agent, or Agent mode

**Usage Analytics**: DAU, WAU, acceptance rate, LoC, model usage, Plan mode telemetry

**Bring-your-own-key (BYOK)** for Copilot **Business and Enterprise** (April 2026, VS Code v1.117): teams connect their own model providers (Azure OpenAI, Bedrock, etc.) directly in VS Code. **Group policies** restrict which domains agents can reach.

**IP Indemnity**: Business & Enterprise only. Microsoft defends copyright claims.

### LAB 4 (10 min)

Students do:
1. Assign a simple issue to @copilot, watch the PR appear
2. Leave a review comment on the PR, see the agent respond
3. Browse enterprise policies (instructor shows content exclusion + audit logs)

---

## Instructor Quick Reference

### Talking Points to Hit
- 2023: autocomplete -> 2024: multimodal -> 2025: autonomous agents -> 2026: agent ecosystems
- ChatGPT side vs Copilot side: Codex CLI vs Copilot CLI, chatgpt.com/codex vs @copilot
- MCP is the universal connector -- build once, use everywhere
- Always verify AI output. Human review required for all agent PRs.
- Premium requests are the cost lever for Copilot

### Side-by-Side Comparison
| | ChatGPT / Codex | GitHub Copilot |
|---|---|---|
| Focus | General AI + coding | Developer workflow |
| Agent | Codex (cloud sandbox) | Coding agent (GitHub VM) |
| CLI | Codex CLI (autonomous) | Copilot CLI (interactive, GA) |
| Enterprise | OpenAI Enterprise / Frontier | GHEC + Copilot Enterprise |
| MCP | 100+ apps via ChatGPT Agent | Built-in GitHub MCP + registry |

### AI Coding Tools Landscape
| Tool | Type | Differentiator |
|------|------|---------------|
| GitHub Copilot | IDE + CLI + Agent | Native GitHub, multi-model |
| Claude Code | CLI agent | 1M context, agent teams (Opus 4.7), Claude Code 2.x |
| Codex CLI | CLI agent | Autonomous task completion |
| Cursor | IDE (VS Code fork) | AI-first editor |
| Windsurf | IDE | Flow-based coding |
| Cline | VS Code extension | Open-source agent |

### Critical Dates
| Date | Event |
|------|-------|
| Dec 2025 | GPT-5.2 released, Visual Studio 2026 GA, MCP donated to AAIF, IntelliCode killed |
| Jan 16, 2026 | ChatGPT Go ($8/mo) launched |
| Jan 22, 2026 | Copilot SDK technical preview |
| Feb 5, 2026 | Claude Opus 4.6 (1M context), OpenAI Frontier launched |
| Feb 13, 2026 | GPT-4o, GPT-4.1, o4-mini retired |
| Feb 17, 2026 | Claude Sonnet 4.6 released |
| Feb 25, 2026 | Copilot CLI GA |
| Feb 26, 2026 | Enterprise AI Controls GA, Claude/Codex for Business/Pro |
| Mar 4, 2026 | Grok Code Fast 1 added to Copilot Free |
| Mar 2026 | GPT-5.3 Instant + Codex + Codex-Spark released |
| Mar 5, 2026 | GPT-5.4 / 5.4 Thinking / 5.4 Pro released |
| Mar 17, 2026 | GPT-5.4 mini and nano released |
| Apr 2-3, 2026 | MCP Dev Summit NYC (~1,200 attendees) |
| Apr 9, 2026 | $100 ChatGPT Pro plan launched (5x Codex vs Plus) |
| Apr 16, 2026 | Claude Opus 4.7 released (3x image res, xhigh effort) |
| Apr 21, 2026 | ChatGPT Images 2.0 (text-in-image rendering) |
| Apr 23-24, 2026 | GPT-5.5 + 5.5 Pro released (chat, then API) |
| Apr 26, 2026 | Sora 2 discontinued globally |
| Apr 30, 2026 | Visual Studio April update -- cloud agents from IDE, Debugger agent |
| May 5, 2026 | **GPT-5.5 Instant becomes ChatGPT default** |
| May 6, 2026 | VS Code April releases blog (v1.116-v1.119 features) |
| May 14, 2026 | Copilot CLI 1.0.48 (token-priced model picker) |
| May 15, 2026 | Grok Code Fast 1 deprecated; ChatGPT Personal Finance preview (US Pro) |
| ~May 15, 2026 | Claude Sonnet 4.8 (new mid-tier default) |
