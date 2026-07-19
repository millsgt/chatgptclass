"""Measure latency, token usage, and a rough cost for a single chat call.

The original version of this file used the removed text-davinci-002 completion
endpoint. It has been rewritten to the Chat Completions API. The point of the
demo is unchanged: send one request, then report how long it took and how many
tokens it consumed so learners can reason about latency and cost.

Requires the OPENAI_API_KEY environment variable.
"""

import os
import time

from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

client = OpenAI(api_key=api_key)

# gpt-5.5 is the everyday default for chat. COST_PER_TOKEN is illustrative only;
# check current pricing at platform.openai.com/pricing before quoting numbers.
MODEL = "gpt-5.5"
COST_PER_TOKEN = 0.00006

prompt = "Hello, how are you?"

# Time the round trip so we can show learners the wall-clock latency.
start_time = time.time()
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
    max_tokens=50,
)
end_time = time.time()

# The SDK returns exact token counts in response.usage. Prefer these over
# guessing from word counts; the model tokenizes differently than str.split().
usage = response.usage
prompt_tokens = usage.prompt_tokens
completion_tokens = usage.completion_tokens
total_tokens = usage.total_tokens
cost = total_tokens * COST_PER_TOKEN

# Clear the console so the metrics read cleanly during a live demo.
os.system("cls" if os.name == "nt" else "clear")

print(response.choices[0].message.content)
print(f"Prompt tokens: {prompt_tokens}")
print(f"Completion tokens: {completion_tokens}")
print(f"Total tokens: {total_tokens}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
print(f"Estimated cost: ${cost:.4f}")
