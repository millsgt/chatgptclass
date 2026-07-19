"""Call a fine-tuned model by name against the Chat Completions API.

Once a fine-tuning job succeeds, OpenAI hands you a model id like
ft:gpt-4.1-mini:my-org:custom-suffix:abc123. You call it exactly like a base
model, just by passing that id as the model argument. This demo shows the
call shape; replace the model id with the one your own job produced.

Requires the OPENAI_API_KEY environment variable.
"""

import os

from openai import OpenAI

# Fail fast if the key is missing so the error names the actual problem.
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Export it before running this demo."
    )

client = OpenAI(api_key=api_key)

# Replace this placeholder with the ft:... id your fine-tuning job returned.
FINE_TUNED_MODEL = "ft:gpt-4.1-mini:my-org:custom-suffix:REPLACE_ME"

completion = client.chat.completions.create(
    model=FINE_TUNED_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful customer service chatbot."},
        {"role": "user", "content": "What are some things I can do with the WonderWidget?"},
    ],
)

# .message is a typed object; .content is the assistant's text.
print(completion.choices[0].message.content)
