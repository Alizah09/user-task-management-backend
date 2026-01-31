from flask import Blueprint, request, jsonify
from database import get_connection

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (title, status, user_id) VALUES (?, ?, ?)",
        (data["title"], data["status"], data["user_id"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task created successfully"})
