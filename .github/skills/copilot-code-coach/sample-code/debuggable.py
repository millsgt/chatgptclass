"""
Survey response aggregator — contains 3 real bugs for Mode 4 (Guided Debug).

Use with the copilot-code-coach skill:
    "debug with me — I'm getting an error running this file"

The bugs are real Python mistakes that produce runtime exceptions.
Do NOT look at the BUGS section below until after you've worked through
the Socratic questions with Copilot Code Coach.

Dataset: datasets/Essentials/Survey Data - recordid_name_age_gender_...csv
"""

import csv
from pathlib import Path
from collections import defaultdict


DATASET = (
    Path(__file__).parent.parent.parent.parent.parent
    / "datasets"
    / "Essentials"
    / "Survey Data - recordid_name_age_gender_edu_emp_income_martialstatus_city_satisfaction_recommendation.csv"
)


def load_responses(filepath: Path) -> list[dict]:
    """Load survey CSV into a list of row dicts."""
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def average_satisfaction(responses: list[dict]) -> float:
    """Return mean satisfaction score across all responses."""
    # BUG 1: satisfaction values are strings from CSV — no conversion to int.
    # This raises: TypeError: unsupported operand type(s) for +: 'int' and 'str'
    total = sum(row["satisfaction"] for row in responses)
    return total / len(responses)


def group_by_city(responses: list[dict]) -> dict[str, list[dict]]:
    """Return responses keyed by city name."""
    groups = defaultdict(list)
    for row in responses:
        groups[row["city"]].append(row)
    return groups


def top_cities(grouped: dict[str, list[dict]], n: int = 3) -> list[tuple[str, float]]:
    """Return top-n cities by average satisfaction, descending."""
    city_avgs = []
    for city, rows in grouped.items():
        # BUG 2: calls average_satisfaction() which has Bug 1, so this cascades.
        # Fix Bug 1 first; once you do, test this independently.
        avg = average_satisfaction(rows)
        city_avgs.append((city, avg))

    # BUG 3: sorts ascending instead of descending — top cities land at the END.
    # Symptom: the "top 3" returned are actually the 3 lowest scorers.
    city_avgs.sort(key=lambda x: x[1])
    return city_avgs[:n]


def report(filepath: Path = DATASET) -> None:
    responses = load_responses(filepath)
    overall = average_satisfaction(responses)
    print(f"Overall satisfaction: {overall:.2f}")

    grouped = group_by_city(responses)
    top = top_cities(grouped)
    print("\nTop 3 cities by satisfaction:")
    for city, score in top:
        print(f"  {city}: {score:.2f}")


if __name__ == "__main__":
    report()


# ─────────────────────────────────────────────────────────────────────────────
# SPOILER — do not read until after the coached debug session
# ─────────────────────────────────────────────────────────────────────────────
#
# Bug 1 (line ~35): int(row["satisfaction"]) — CSV values are strings
# Bug 2 (line ~49): cascades from Bug 1; no independent fix needed
# Bug 3 (line ~54): city_avgs.sort(key=lambda x: x[1], reverse=True)
#
