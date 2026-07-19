# Hands-On Labs

This directory holds the four hands-on labs for the course, one per teaching hour. Each lab is self-contained and followable in about 5-10 minutes, and each maps to a segment in `course-plan-may-2026.md`.

## Structure

```
labs/
├── hour-1-chatgpt/
│   └── lab-01-image-to-code.md      # ChatGPT Projects, custom GPTs, and Tasks
├── hour-2-chatgpt/
│   └── lab-02-codex-and-data.md     # Codex cloud agent + Data Analysis to PowerPoint
├── hour-3-copilot/
│   └── lab-03-copilot-modes.md      # Copilot chat modes and custom instructions
└── hour-4-copilot/
    └── lab-04-coding-agent.md       # Copilot coding agent (@copilot) end-to-end
```

## Labs at a Glance

| Lab | Hour | Summary |
|-----|------|---------|
| **Lab 1** | Hour 1 (ChatGPT Power User) | Create a **Project** with HR data, build a custom **"HR Assistant" GPT** with Code Interpreter, and schedule a recurring **Task**. |
| **Lab 2** | Hour 2 (ChatGPT for Builders) | Assign a GitHub issue to the **Codex** cloud agent, then use **Data Analysis** to turn a market-data CSV into 3 charts and export to **PowerPoint**. |
| **Lab 3** | Hour 3 (Copilot in the Editor) | Compare the four Copilot chat modes (**Ask, Edit, Agent, Plan**) on one prompt, add `.github/copilot-instructions.md`, and practice context variables. |
| **Lab 4** | Hour 4 (Copilot Beyond the Editor) | Assign an issue to the **@copilot** coding agent, iterate on the resulting PR via review comments, and observe enterprise policy controls. |

## Datasets

Labs reference sample data under `datasets/`. Lab 2 uses `datasets/Financial/Wall Street Market Data - Fictional.csv` (columns: **Symbol, Date, Open, High, Low, Close, Volume**). Lab 1 uses `datasets/Human Resources/HRIS.csv`.
