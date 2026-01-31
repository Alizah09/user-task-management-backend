from flask import Blueprint, request, jsonify
from database import get_connection

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User created successfully"})
