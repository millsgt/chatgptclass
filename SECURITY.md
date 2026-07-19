# Security Guidelines

## Secret Scanning

This repository is configured with both local and GitHub-based secret scanning to prevent credentials and other sensitive information from being committed and pushed to the repository.

### Local Pre-commit Hook

A pre-commit hook is installed that scans all staged changes for potential secrets before allowing a commit. This provides immediate feedback during development.

To ensure you have the hook enabled:

1. Make sure Python is installed on your system
2. Install the detect-secrets package:
   ```
   pip install detect-secrets
   ```
3. The pre-commit hook should be automatically enabled. If not, you can manually copy it:
   ```
   cp .git/hooks/pre-commit.sample .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

### GitHub Actions Workflow

The GitHub Actions workflow at **`.github/workflows/secret-scanning.yml`** runs on pull requests and pushes to the default branch. This is the live, committed layer of protection in this repository.

### Managing False Positives (recommended baseline workflow)

This repo does not ship a `.secrets.baseline` file. If you want to adopt one to suppress verified false positives, generate it locally and commit it:

1. Create the baseline:
   ```
   python -m detect_secrets scan > .secrets.baseline
   ```
2. Audit and mark false positives:
   ```
   python -m detect_secrets audit .secrets.baseline
   ```
3. Re-scan against the baseline going forward:
   ```
   python -m detect_secrets scan --baseline .secrets.baseline
   ```

### Best Practices

1. **Never** commit credentials, API keys, or other secrets to the repository.
2. Use environment variables or a secure secrets manager for all sensitive values.
3. Use the committed **`.env.example`** template to document required environment variables without values, then copy it to a git-ignored `.env` for local runs.
4. Rotate any credentials that have been accidentally committed, even if removed later (Git history preserves them). 