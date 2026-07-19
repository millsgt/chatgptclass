"""Entrypoint for the Flask chat demo.

    python run.py

Then open http://127.0.0.1:5000. Requires OPENAI_API_KEY in the environment
(or a .env file next to this script).
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True gives auto-reload and tracebacks for live teaching. Turn it off
    # for anything resembling production.
    app.run(host="127.0.0.1", port=5000, debug=True)
