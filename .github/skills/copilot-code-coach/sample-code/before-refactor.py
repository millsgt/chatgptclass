"""
Employee salary report generator.

Intentionally contains teaching-grade issues for use with the
copilot-code-coach skill (Modes 3, 4, and 5).

Exercise prompt:
    1. Use Mode 3 (Teaching Review) to find all issues.
    2. Use Mode 5 (Refactor Narrative) to produce a clean version.
    3. Count how many distinct code-quality principles were violated.
"""

import csv
import os


# ── Issue 1: magic number (no named constant) ────────────────────────────────
BONUS_RATE = 0.1   # this one is fine — but the threshold below is not

def calculate_bonus(salary):
    # Issue 2: magic number — what does 50000 mean?
    if salary > 50000:
        return salary * BONUS_RATE
    return 0


# ── Issue 3: god function — does loading, filtering, computing, AND printing ──
def process_employees(filepath):
    employees = []

    # Issue 4: no error handling around file I/O
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append(row)

    total_payroll = 0
    bonuses = []

    for emp in employees:
        # Issue 5: no input validation — salary could be empty string or missing
        salary = float(emp["salary"])
        bonus = calculate_bonus(salary)
        total_payroll += salary

        # Issue 6: mutation inside loop — modifying the dict we're iterating
        emp["bonus"] = bonus
        bonuses.append(bonus)

    # Issue 7: print instead of return / logging
    print("Total payroll:", total_payroll)
    print("Total bonuses:", sum(bonuses))

    # Issue 8: no return value — caller can't use the result
    for emp in employees:
        print(emp["firstname_lastname"], "-", emp["salary"], "-", emp["bonus"])


# ── Issue 9: hardcoded path — breaks on every other machine ──────────────────
if __name__ == "__main__":
    process_employees(r"C:\Users\timot\datasets\Employee Data.csv")
