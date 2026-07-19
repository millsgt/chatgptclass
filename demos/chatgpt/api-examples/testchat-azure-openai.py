"""Minimal Azure OpenAI chat call with the v1.x AzureOpenAI client.

The original file used the removed openai.api_type / openai.api_base globals and
the Completion endpoint. This version uses the modern client and Chat
Completions. Secrets come from environment variables, never hardcoded.

Set before running:
  AZURE_OPENAI_ENDPOINT     e.g. https://my-resource.openai.azure.com/
  AZURE_OPENAI_KEY          the resource key from the Azure portal
  AZURE_OPENAI_DEPLOYMENT   your deployment name from Azure OpenAI Studio
"""

import os

from openai import AzureOpenAI

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
api_key = os.environ.get("AZURE_OPENAI_KEY")
deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT")

missing = [
    name
    for name, value in (
        ("AZURE_OPENAI_ENDPOINT", endpoint),
        ("AZURE_OPENAI_KEY", api_key),
        ("AZURE_OPENAI_DEPLOYMENT", deployment_name),
    )
    if not value
]
if missing:
    raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

# api_version pins the Azure REST contract; 2024-10-21 is a current GA version.
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21",
)

print("Sending a test chat completion to Azure...")
response = client.chat.completions.create(
    model=deployment_name,  # on Azure, model = your deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the Kentucky Derby in 1966?"},
    ],
    max_tokens=50,
    temperature=0.7,
)

print(response.choices[0].message.content)
