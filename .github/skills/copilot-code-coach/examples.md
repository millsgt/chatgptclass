# GitHub Copilot Code Coach — Examples & Invocation Guide

A reference card for students learning to use the `copilot-code-coach` skill inside VS Code.

---

## Quick-Start: How to Invoke the Skill

Open GitHub Copilot Chat (`Ctrl+Alt+I`) and type one of the phrases below.
The skill activates automatically based on your wording.

---

## Mode 1 · Explain Mode

**Trigger phrases**
```
explain this code
what does this do?
walk me through this function
break this down for me
```

**Example session**
```
User: explain this code
      [with the contents of demos/copilot/main.py selected]

Copilot Code Coach:
  ### What This Code Does
  Calls the OpenAI API to fetch the etymology of a name entered by the user.

  ### Block-by-Block Walkthrough
  **Block 1 — get_etymology()**
  - Does: Sends a system + user message pair to the GPT model and returns the reply.
  - Why: The system message primes the model to answer only as an etymology specialist,
    reducing off-topic responses.
  - If removed: The program has no way to query OpenAI; it would crash with a NameError.
  ...
```

---

## Mode 2 · Exercise Generator

**Trigger phrases**
```
generate exercises about list comprehensions
give me practice problems for async/await
create a novice/practitioner/expert drill for SQL joins
```

**Example session**
```
User: generate practice exercises for Python error handling

Copilot Code Coach:
  ### Novice Exercise — Spot the Gap
  The function below has no error handling. Add a try/except block so that
  a missing file prints a friendly message instead of crashing.

  ```python
  def read_config(path):
      with open(path) as f:
          return f.read()
  ```
  **Success criteria**: FileNotFoundError is caught; program continues running.
  **Hint**: Which exception does `open()` raise when a file is missing?

  <details><summary>Solution</summary>
  ...
  </details>
```

---

## Mode 3 · Teaching Review

**Trigger phrases**
```
code review for learning
annotate this with teaching notes
review and explain every issue you find
```

**Example session**
```
User: code review for learning
      [with demos/vulnerable-code selected]

Copilot Code Coach:
  #### CRITICAL: SQL Injection Vector
  **Line**: 42
  **What**: User input is concatenated directly into an SQL string.
  **Why it matters**: An attacker can terminate the query and inject arbitrary SQL
    (OWASP A03:2021 — Injection).
  **Improved version**:
  ```python
  cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
  ```
  **Concept to study**: Parameterised queries / prepared statements
```

---

## Mode 4 · Guided Debug

**Trigger phrases**
```
debug with me
help me find the bug
I'm getting [error] - walk me through it
```

**Example session**
```
User: debug with me — I'm getting KeyError: 'salary' on line 18

Copilot Code Coach:
  Let's narrow this down together.

  Question 1 (Broad): What does your input data look like? Is it coming from a file,
  an API, or user input?

  [learner answers]

  Clue: KeyError means the dictionary does not have the key you're asking for.
  Before we look at line 18, where does this dictionary get populated?

  [learner answers]

  Question 2 (Mid): Which block of code do you think builds or loads the dictionary?
  ...
```

---

## Mode 5 · Refactor Narrative

**Trigger phrases**
```
refactor and explain
clean this up and tell me why
show me a better version and explain every change
```

**Example session**
```
User: refactor and explain the get_etymology function in main.py

Copilot Code Coach:
  | # | What Changed | Principle Applied |
  |---|-------------|-------------------|
  | 1 | Extracted prompt strings into constants | Magic-string elimination |
  | 2 | Replaced nested try/except with single handler | DRY / readability |
  | 3 | Added type hints | Self-documenting code |
  | 4 | Renamed `response` to `api_response` | Intention-revealing names |
```

---

## Mode 6 · Concept Deep-Dive

**Trigger phrases**
```
teach me about decorators
explain closures to me
I don't understand async/await
deep dive into RBAC
```

**Example session**
```
User: teach me about Python decorators

Copilot Code Coach:
  **Definition**: A decorator is a function that wraps another function to add
  behaviour before or after it runs, without modifying the original function's body.

  **Mental model**: Think of a decorator like a TSA security checkpoint before a
  flight gate — every passenger (function call) passes through the same screening
  (wrapper logic) before reaching their destination (the original function).

  **Minimal working example**:
  ```python
  def timer(func):
      import time
      def wrapper(*args, **kwargs):
          start = time.perf_counter()
          result = func(*args, **kwargs)
          print(f"{func.__name__} ran in {time.perf_counter() - start:.4f}s")
          return result
      return wrapper

  @timer
  def load_data(path):
      with open(path) as f:
          return f.read()
  ```
  ...
```

---

## Tips for Learners

- **Select code before invoking** — the skill uses your selection as context.
- **Be specific about your level** — "I'm new to Python" vs "I know Python but not async".
- **Ask follow-up questions freely** — the skill is designed for conversation, not one-shot answers.
- **Use the sample files** in `.github/skills/copilot-code-coach/sample-code/` as playground targets.
