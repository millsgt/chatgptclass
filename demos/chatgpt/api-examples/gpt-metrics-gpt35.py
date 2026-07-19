"""Report token usage and latency for a chat completion, using response.usage.

Companion to gpt-metrics-davinci.py. This one keeps a system+user message pair
and reads exact token counts from the typed usage object instead of estimating.

Requires the OPENAI_API_KEY environment variable.
"""

import os
import time

from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

client = OpenAI(api_key=api_key)

# gpt-5.5 is the everyday chat default. COST_PER_TOKEN is illustrative only;
# confirm current pricing at platform.openai.com/pricing.
MODEL = "gpt-5.5"
COST_PER_TOKEN = 0.0002

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate the following English text to French: 'Hello, world'"},
]

start_time = time.time()
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
)
end_time = time.time()

print(f"Prompt: {messages}")
# Typed object access, not dict indexing - that pre-1.0 pattern was removed.
print(f"Completion: {response.choices[0].message.content}")

usage = response.usage
print(f"Prompt token length: {usage.prompt_tokens}")
print(f"Completion token length: {usage.completion_tokens}")
print(f"Overall token length: {usage.total_tokens}")
print(f"Time taken to generate the completion: {end_time - start_time:.2f} seconds")
print(f"Cost: {usage.total_tokens * COST_PER_TOKEN} USD")
