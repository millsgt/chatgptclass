<#
.SYNOPSIS
    Pre-class asset and freshness linter for the ChatGPT + GitHub Copilot course.

.DESCRIPTION
    Run this before every delivery. It catches the two failure modes that have bitten this
    course: (1) the course plan or labs referencing a dataset/file path that does not exist on
    disk (the phantom sales_data.csv problem), and (2) stale model names, versions, or install
    commands that a sharp student would flag as out of date on stage.

    The check is intentionally simple and fast. It greps the plan, labs, README, and CLAUDE.md
    for every datasets/... path and asserts the file is present, then scans for a list of known
    stale tokens that should never appear in current content. Exit code is non-zero if anything
    fails, so this can gate a commit or CI run.

.PARAMETER RepoRoot
    Path to the repo root. Defaults to two levels up from this script (scripts/utilities/..).

.EXAMPLE
    pwsh ./scripts/utilities/preflight-check.ps1
    Runs all checks against the current repo and prints a pass/fail summary.

.NOTES
    Update $StaleTokens each delivery cycle as the technology landscape moves. The whole point is
    that this list is the single place you refresh, not scattered across the deck and docs.
#>
[CmdletBinding()]
param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
)

$ErrorActionPreference = 'Stop'
$failures = 0

Write-Host "Pre-flight check for: $RepoRoot" -ForegroundColor Cyan
Write-Host ("-" * 60)

# Content files students and the instructor actually follow.
$contentFiles = @(
    'course-plan-july-2026.md'
    'whats-new-july-2026.md'
    'README.md'
    'CLAUDE.md'
) + (Get-ChildItem -Path (Join-Path $RepoRoot 'labs') -Filter '*.md' -Recurse | ForEach-Object { $_.FullName })

# --- Check 1: every datasets/... path referenced in content exists on disk ---
# Match datasets/ paths up to the file extension, allowing spaces in filenames (the CSVs
# in this repo have spaces), stopping at a closing quote, backtick, paren, or newline.
Write-Host "`n[1] Dataset path references resolve to real files"
$datasetRefs = foreach ($f in $contentFiles) {
    $full = if ([IO.Path]::IsPathRooted($f)) { $f } else { Join-Path $RepoRoot $f }
    if (-not (Test-Path $full)) { continue }
    Select-String -Path $full -Pattern 'datasets/[^`"''\)\r\n]+?\.(csv|json|xlsx|jsonl)' -AllMatches |
        ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }
}
$datasetRefs = $datasetRefs | Sort-Object -Unique
foreach ($ref in $datasetRefs) {
    $target = Join-Path $RepoRoot ($ref -replace '/', '\')
    if (Test-Path -LiteralPath $target) {
        Write-Host "  OK   $ref" -ForegroundColor Green
    } else {
        Write-Host "  MISS $ref  (referenced but not on disk)" -ForegroundColor Red
        $failures++
    }
}
if (-not $datasetRefs) { Write-Host "  (no dataset references found)" }

# --- Check 2: no known-stale tokens in current content ---
# Refresh this list each delivery. Left side is the stale token, right side is the reason.
$StaleTokens = @{
    'GPT-5.2'                        = 'superseded by GPT-5.6 (Jul 2026)'
    'Claude Opus 4.6'                = 'superseded by Opus 4.8'
    'Claude Opus 4.7'                = 'superseded by Opus 4.8'
    'Claude Sonnet 4.6'              = 'superseded by Sonnet 5'
    'Claude Sonnet 4.8'              = 'superseded by Sonnet 5 (GA Jun 30 2026)'
    'v1.0.48'                        = 'Copilot CLI is v1.0.71 (Jul 16 2026)'
    '@github/copilot-cli'            = 'package is @github/copilot'
    'server-github'                  = 'deprecated GitHub MCP package; use hosted server'
    'sales_data.csv'                 = 'phantom dataset; use Wall Street Market Data CSV'
    'March 2026'                     = 'delivery is July 2026'
    'sdk": "^0.5'                    = 'MCP SDK should be ^1.29.0'
}
Write-Host "`n[2] No stale model names, versions, or commands in content"
# The whats-new file is a historical timeline. Past model names (GPT-5.2, Opus 4.6...) are
# legitimate history there, so it is exempt from the model-name checks. Install-command and
# phantom-dataset tokens are still checked everywhere, because those are never "history".
$modelTokens = 'GPT-5.2', 'Claude Opus 4.6', 'Claude Opus 4.7', 'Claude Sonnet 4.6', 'Claude Sonnet 4.8', 'March 2026'
foreach ($f in $contentFiles) {
    $full = if ([IO.Path]::IsPathRooted($f)) { $f } else { Join-Path $RepoRoot $f }
    if (-not (Test-Path $full)) { continue }
    $isTimeline = $full -match 'whats-new'
    foreach ($tok in $StaleTokens.Keys) {
        if ($isTimeline -and ($modelTokens -contains $tok)) { continue }  # history, not a stale claim
        $lines = Select-String -LiteralPath $full -Pattern ([regex]::Escape($tok)) -AllMatches
        foreach ($ln in $lines) {
            # Skip lines that TEACH the correction rather than commit the error.
            if ($ln.Line -match 'phantom|superseded|deprecat|never existed|replaced|old plan|NOT |Not @|prior|retired|shut down') { continue }
            # Skip dated-history rows: a Markdown table row whose first cell is a date
            # (e.g. "| Dec 2025 | ..." or "| Feb 5, 2026 | ..."). Timelines name old models on purpose.
            if ($ln.Line -match '^\s*\|\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d') { continue }
            $rel = $full.Replace($RepoRoot, '').TrimStart('\')
            Write-Host ("  STALE {0}:{1}  '{2}'  ({3})" -f $rel, $ln.LineNumber, $tok, $StaleTokens[$tok]) -ForegroundColor Red
            $failures++
        }
    }
}
if ($failures -eq 0) { Write-Host "  OK   no stale tokens found" -ForegroundColor Green }

# --- Check 3: no live-format OpenAI keys committed in demos/apps ---
Write-Host "`n[3] No hardcoded OpenAI keys in demos or apps"
$keyHits = Get-ChildItem -Path (Join-Path $RepoRoot 'demos'), (Join-Path $RepoRoot 'apps') -Include '*.py','*.js','*.md' -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch 'node_modules' } |
    Select-String -Pattern 'sk-[A-Za-z0-9]{20,}' -AllMatches |
    Where-Object { $_.Line -notmatch 'sk-your-key|sk-test|os\.environ|example' }
foreach ($hit in $keyHits) {
    Write-Host ("  KEY  {0}:{1}" -f $hit.Filename, $hit.LineNumber) -ForegroundColor Red
    $failures++
}
if (-not $keyHits) { Write-Host "  OK   no live-format keys" -ForegroundColor Green }

Write-Host "`n$("-" * 60)"
if ($failures -eq 0) {
    Write-Host "PRE-FLIGHT PASS: repo is stage-ready." -ForegroundColor Green
    exit 0
} else {
    Write-Host "PRE-FLIGHT FAIL: $failures issue(s) above. Fix before delivery." -ForegroundColor Red
    exit 1
}
