"""Interactive etymology lookup built on the Chat Completions API.

Prompts for a first name, asks the model for its etymology, and prints the
reply. Shows a clean try/except around a single API call plus a fail-fast check
for the API key.

Requires the OPENAI_API_KEY environment variable.
"""

import os

from openai import OpenAI


def get_etymology(client: OpenAI, name: str) -> str:
    """Return the etymology of name, or a readable error string on failure."""
    try:
        response = client.chat.completions.create(
            model="gpt-5.5",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an etymology specialist. You provide the etymology "
                        "of a name, the meaning of the name, and its trend in "
                        "popularity over time."
                    ),
                },
                {
                    "role": "user",
                    "content": f"What is the etymology of the name {name}?",
                },
            ],
        )
        # Typed access on the v1.x response object; the removed pre-1.0 SDK used
        # message["content"] dict indexing here.
        return response.choices[0].message.content
    except Exception as e:  # fixed the original 'ecept' typo
        return f"An error occurred: {e}"


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
        )
        return

    # Build the client once and pass it in, so the demo shows reuse.
    client = OpenAI(api_key=api_key)

    name = input("Enter a first name: ")
    etymology = get_etymology(client, name)

    print("\nEtymology:")
    print(etymology)


if __name__ == "__main__":
    main()
