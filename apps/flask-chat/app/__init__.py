"""Flask app factory for the OpenAI chat demo.

create_app() builds the app, loads the OPENAI_API_KEY from the environment (or a
local .env via python-dotenv), and registers one page plus a /chat POST route
that relays the user's prompt to the Chat Completions API.

Run it via run.py. Set OPENAI_API_KEY before starting.
"""

import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from openai import OpenAI


def create_app() -> Flask:
    # Load a local .env if present so students can keep the key out of shell
    # history. Real deployments inject the variable directly.
    load_dotenv()

    app = Flask(__name__)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Export it before running.")

    # Build the client once at startup and reuse it across requests.
    client = OpenAI(api_key=api_key)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/chat", methods=["POST"])
    def chat():
        # Guard against an empty prompt before spending an API call.
        prompt = (request.json or {}).get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Please enter a prompt."}), 400

        try:
            response = client.chat.completions.create(
                model="gpt-5.5",  # everyday chat default for this delivery
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=500,
            )
            reply = response.choices[0].message.content
        except Exception as error:  # surface one readable message to the UI
            return jsonify({"error": f"API error: {error}"}), 502

        return jsonify({"reply": reply})

    return app
