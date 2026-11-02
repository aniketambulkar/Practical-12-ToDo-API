import pytest

import app as todo_app
from app import app


@pytest.fixture
def client():
    todo_app.tasks.clear()
    todo_app.next_task_id = 1

    with app.test_client() as test_client:
        yield test_client

    todo_app.tasks.clear()
    todo_app.next_task_id = 1


def test_add_task_successfully(client):
    response = client.post(
        "/tasks",
        json={"title": "Study", "description": "Review Flask"},
    )

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "title": "Study",
        "description": "Review Flask",
        "completed": False,
    }


def test_add_task_without_title_returns_400(client):
    response = client.post("/tasks", json={"description": "Review Flask"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "A non-empty title is required."}


def test_retrieve_all_tasks(client):
    client.post("/tasks", json={"title": "Study", "description": "Review Flask"})
    client.post("/tasks", json={"title": "Exercise", "description": "Go for a walk"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "title": "Study",
            "description": "Review Flask",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Exercise",
            "description": "Go for a walk",
            "completed": False,
        },
    ]


def test_complete_task_successfully(client):
    client.post("/tasks", json={"title": "Study", "description": "Review Flask"})

    response = client.put("/tasks/1")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "title": "Study",
        "description": "Review Flask",
        "completed": True,
    }


def test_complete_task_with_invalid_id_returns_404(client):
    response = client.put("/tasks/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Task not found."}


def test_delete_task_successfully(client):
    client.post("/tasks", json={"title": "Study", "description": "Review Flask"})

    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Task deleted successfully.",
        "task": {
            "id": 1,
            "title": "Study",
            "description": "Review Flask",
            "completed": False,
        },
    }
    assert client.get("/tasks").get_json() == []


def test_delete_task_with_invalid_id_returns_404(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Task not found."}