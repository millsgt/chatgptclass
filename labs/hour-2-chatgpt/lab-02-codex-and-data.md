# Lab 2: Codex Cloud Agent and Data Analysis to PowerPoint

## Objective
Use OpenAI Codex (powered by GPT-5.3-Codex, with the GPT-5.6 family now current as of July 9, 2026) to assign a coding task from a GitHub issue, then use ChatGPT Data Analysis to turn a financial CSV into charts and export them to PowerPoint.

## Prerequisites
- ChatGPT Plus or Pro subscription
- GitHub account linked to chatgpt.com/codex (or follow along with instructor demo)
- Dataset: `datasets/Financial/Wall Street Market Data - Fictional.csv`
- Optional: Node.js installed for Codex CLI

## Steps

### Part A: Codex Cloud Agent

1. **Open Codex**
   - Navigate to [chatgpt.com/codex](https://chatgpt.com/codex).
   - If this is your first visit, connect your GitHub account when prompted.

2. **Assign a GitHub issue**
   - Select a repository and pick an open issue (or create a small one such as "Add a health-check endpoint").
   - Click **Start task**. The async agent starts work in the background.
   - While it runs, review a previously completed task to see the PR diff and merge status.

3. **No Codex access?**
   - Follow the instructor's live demo and note the workflow: issue assigned, sandbox created, branch created, PR opened.

### Part B: Data Analysis to PowerPoint

4. **Upload the dataset**
   - In a new ChatGPT conversation, upload `datasets/Financial/Wall Street Market Data - Fictional.csv`.
   - Columns: **Symbol, Date, Open, High, Low, Close, Volume**.

5. **Generate charts and export**
   - Prompt: **"Create 3 charts: closing price trend over time, daily volume, and daily returns distribution. Then export to PowerPoint."**
   - Review the generated charts (closing price line, daily volume bars, and a histogram of daily returns).

6. **Download the PowerPoint**
   - Click the download link to save the `.pptx` file.
   - Open it locally and verify the charts rendered correctly.

### Part C: Codex CLI (if time permits)

7. **Install and run Codex CLI**
   ```bash
   npm i -g @openai/codex
   codex "explain this codebase structure"
   ```
   - Review the output and note the approval mode (Auto, Read Only, Full Access).

## Demo Tips
- Codex cloud tasks run asynchronously -- you can queue multiple issues and check back later.
- Data Analysis runs Python (pandas, matplotlib, plotly) in a sandbox and handles files up to 512 MB.
- Compare Codex CLI (autonomous, long-running tasks) with Copilot CLI (interactive terminal agent) when students ask about the difference.
