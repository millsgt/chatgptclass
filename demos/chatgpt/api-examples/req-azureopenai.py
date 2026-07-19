"""Call Azure OpenAI with the v1.x AzureOpenAI client.

Azure OpenAI differs from OpenAI in three ways this demo highlights:
  1. You authenticate against your own resource endpoint, not api.openai.com.
  2. You pass a deployment name (your custom name for a deployed model) as the
     model argument, not a public model id.
  3. You pin an api_version.

All secrets come from environment variables. Set these before running:
  AZURE_OPENAI_ENDPOINT   e.g. https://my-resource.openai.azure.com/
  AZURE_OPENAI_KEY        the resource key from the Azure portal
  AZURE_OPENAI_DEPLOYMENT the deployment name you chose in Azure OpenAI Studio
"""

import os

from openai import AzureOpenAI

# Fail fast, and name each missing variable so the fix is obvious.
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

# api_version pins the Azure REST contract. 2024-10-21 is a current GA version;
# check learn.microsoft.com for the latest before shipping.
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21",
)

print("Sending a test chat completion to Azure OpenAI...")
response = client.chat.completions.create(
    model=deployment_name,  # deployment name stands in for the model id on Azure
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a tagline for an ice cream shop."},
    ],
    max_tokens=32,
)

print(response.choices[0].message.content)
