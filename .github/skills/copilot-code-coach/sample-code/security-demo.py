"""
Patient data lookup API — teaching-grade security demo.

Contains intentional OWASP Top 10 violations for use with the
copilot-code-coach skill (Mode 3: Teaching Review — security focus).

DO NOT deploy this code. It is an instructional artifact only.

Learning objectives:
    - Identify OWASP A01 (Broken Access Control)
    - Identify OWASP A02 (Cryptographic Failures)
    - Identify OWASP A03 (Injection)
    - Identify OWASP A07 (Identification and Authentication Failures)
    - Practice using Copilot Code Coach to annotate and fix each finding
"""

import sqlite3
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# ── OWASP A02: Cryptographic Failure ─────────────────────────────────────────
# WHY THIS IS BAD: MD5 is cryptographically broken. Use bcrypt or argon2.
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# ── OWASP A07: Hardcoded credential ──────────────────────────────────────────
# WHY THIS IS BAD: Any developer with repo access has the admin password.
ADMIN_PASSWORD_HASH = hash_password("admin123")


def get_db():
    # WHY THIS IS BAD (A02): Database in-memory is fine for tests, but a real
    # deployment using a file path with no encryption exposes PHI at rest.
    return sqlite3.connect("patients.db")


@app.route("/patient")
def get_patient():
    # ── OWASP A03: SQL Injection ──────────────────────────────────────────────
    # WHY THIS IS BAD: f-string interpolation lets an attacker pass:
    #   ?id=1 OR 1=1--
    # which dumps the entire patients table.
    patient_id = request.args.get("id")
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM patients WHERE patient_id = '{patient_id}'"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({"patient": row})


@app.route("/admin/patients")
def list_all_patients():
    # ── OWASP A01: Broken Access Control ─────────────────────────────────────
    # WHY THIS IS BAD: Any authenticated user (even a receptionist) can call
    # this endpoint and retrieve all patient records. No role check at all.
    password = request.headers.get("X-Admin-Password", "")
    if hash_password(password) != ADMIN_PASSWORD_HASH:
        return jsonify({"error": "unauthorized"}), 401

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({"patients": rows})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # ── OWASP A07: Verbose error message leaks valid usernames ───────────────
    # WHY THIS IS BAD: Returning different messages for "wrong username" vs
    # "wrong password" lets attackers enumerate valid accounts.
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT password_hash FROM users WHERE username = '{username}'")
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": "Username not found"}), 401   # leaks info!
    if row[0] != hash_password(password):
        return jsonify({"error": "Wrong password"}), 401        # leaks info!

    return jsonify({"message": "Login successful"})


if __name__ == "__main__":
    # ── Misconfiguration: debug=True in any non-dev environment ──────────────
    app.run(debug=True, host="0.0.0.0", port=5000)
