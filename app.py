from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_task_id = 1


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_task_id

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required."}), 400

    description = data.get("description", "")
    if not isinstance(description, str):
        return jsonify({"error": "Description must be a string."}), 400

    task = {
        "id": next_task_id,
        "title": title.strip(),
        "description": description,
        "completed": False,
    }
    tasks.append(task)
    next_task_id += 1

    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return jsonify(task), 200

    return jsonify({"error": "Task not found."}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)
            return jsonify({
                "message": "Task deleted successfully.",
                "task": deleted_task,
            }), 200

    return jsonify({"error": "Task not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
