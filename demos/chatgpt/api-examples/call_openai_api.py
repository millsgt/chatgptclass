"""Reusable helper that sends a string to the OpenAI API and prints the reply.

This is the worked answer to the prompt we hand students on stage:

    "Write a function that accepts string input and sends it to the OpenAI API.
     The function should return the API's response formatted in a visually
     appealing way."

It wraps a single Chat Completions call in error handling so a bad key or a
network hiccup surfaces a readable message instead of a stack trace.

Requires the OPENAI_API_KEY environment variable.
"""

import os
import textwrap

from openai import OpenAI


def ask_openai(user_input: str, model: str = "gpt-5.5") -> str:
    """Send user_input to the model and return the reply wrapped for display.

    We build a fresh client per call for demo clarity; in a real app you would
    construct the client once and reuse it. gpt-5.5 is the everyday default.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        # Raise rather than return so callers cannot mistake the error for a
        # normal model reply.
        raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a concise, helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
    except Exception as error:  # noqa: BLE001 - demo wants one readable message
        return f"An error occurred while calling the OpenAI API: {error}"

    reply = response.choices[0].message.content or ""
    # Wrap to a fixed width so long answers read cleanly in a terminal.
    return "\n".join(textwrap.wrap(reply, width=80)) or "(empty response)"


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("\n" + ask_openai(prompt))
