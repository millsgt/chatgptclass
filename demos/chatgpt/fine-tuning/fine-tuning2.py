"""Upload training data, then start a fine-tuning job with the v1.x SDK.

A shorter companion to fine-tuning.py that just shows the upload-then-create
handoff: the file id from client.files.create feeds client.fine_tuning.jobs.create.

The original used the removed openai.File.create and openai.FineTuningJob.create
top-level classes.

Requires the OPENAI_API_KEY environment variable.
"""

import os

from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

client = OpenAI(api_key=api_key)

# Verify the current fine-tunable model list at
# platform.openai.com/docs/guides/fine-tuning.
BASE_MODEL = "gpt-4.1-mini"

# Upload the training data. purpose="fine-tune" tags the file for job use.
training_file = client.files.create(
    file=open("fine-tuning-dataset.jsonl", "rb"),
    purpose="fine-tune",
)
print(f"Uploaded file id: {training_file.id}")

# Create the fine-tuned model from that file id.
job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model=BASE_MODEL,
)
print(f"Started fine-tuning job: {job.id} (status: {job.status})")
