"""Kick off a fine-tuning job and poll it to completion with the v1.x SDK.

Flow this demo shows:
  1. Upload a JSONL training file with client.files.create(purpose="fine-tune").
  2. Start a job with client.fine_tuning.jobs.create(...).
  3. Poll client.fine_tuning.jobs.retrieve(...) until it succeeds or fails.

The original file used the removed openai.FineTuning / openai.Validation
top-level classes. Those are gone in openai>=1.x.

Requires the OPENAI_API_KEY environment variable.
"""

import os
import time

from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

client = OpenAI(api_key=api_key)

# gpt-4.1-mini is a commonly fine-tunable base model. Verify the current
# fine-tunable model list at platform.openai.com/docs/guides/fine-tuning.
BASE_MODEL = "gpt-4.1-mini"
TRAINING_FILE = "fine-tuning-dataset.jsonl"

# Step 1: upload the training data. The returned object carries the file id
# the job will reference.
training_file = client.files.create(
    file=open(TRAINING_FILE, "rb"),
    purpose="fine-tune",
)
print(f"Uploaded training file: {training_file.id}")

# Step 2: start the fine-tuning job against that file.
job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model=BASE_MODEL,
)
print(f"Started fine-tuning job: {job.id}")

# Step 3: poll until the job reaches a terminal state. Polling every 60s keeps
# us well under any rate limits for a teaching demo.
while True:
    job = client.fine_tuning.jobs.retrieve(job.id)
    print(f"Job status: {job.status}")

    if job.status in ("succeeded", "failed", "cancelled"):
        break

    time.sleep(60)

if job.status == "succeeded":
    # On success the job carries the id of your new fine-tuned model. Call it
    # like any other model (see completion.py).
    print(f"Fine-tuned model ready: {job.fine_tuned_model}")
else:
    print(f"Fine-tuning did not succeed. Final status: {job.status}")
