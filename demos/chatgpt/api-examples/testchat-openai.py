"""Multi-turn chat demo against the OpenAI Chat Completions API.

Demonstrates how a conversation is really just a running list of role-tagged
messages that you resend on every turn. The model has no memory of its own, so
the full transcript (system, user, assistant, user) is the context you pass in.

Requires the OPENAI_API_KEY environment variable. Never hardcode the key here.
"""

import os

from openai import OpenAI

# Read the secret from the environment. Fail fast with a clear message rather
# than letting the SDK raise a vaguer error deeper in the call stack.
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Export it first, for example: "
        "$env:OPENAI_API_KEY = '<your-key>' in PowerShell."
    )

# The v1.x client is the object you call for every request. Passing the key
# explicitly is equivalent to the SDK reading it from the env on its own, but
# it makes the dependency obvious to learners.
client = OpenAI(api_key=api_key)

# gpt-5.5 is the everyday chat default as of this course delivery. Swap the
# model string to try a different tier without touching the rest of the code.
response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like today?"},
        {
            "role": "assistant",
            "content": (
                "I'm an AI and I don't have access to real-time data. However, "
                "you can check the weather on a weather website or app."
            ),
        },
        {
            "role": "user",
            "content": "Translate the following English text to French: 'Hello, how are you?'",
        },
    ],
)

# In the v1.x SDK the result is a typed object, not a dict. Reach into the
# first choice's message content with attribute access, not ['...'] indexing.
print(response.choices[0].message.content)
