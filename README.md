# AI-Assisted To-Do List REST API

## Project Description
A simple To-Do List REST API developed using Python Flask with AI assistance throughout the Software Development Life Cycle (SDLC).

## Features
- Add new tasks.
- View all tasks.
- Mark tasks as completed.
- Delete tasks.
- JSON-based API responses.

## Technologies Used
- Python
- Flask
- Pytest
- Bandit
- OpenAPI 3.0
- Git and GitHub

## Installation

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

Application URL: http://127.0.0.1:5000

## Run Tests

```bash
python -m pytest -v
```

## Security Scan

```bash
python -m bandit -r . -x ./venv
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /tasks | Add task |
| GET | /tasks | View tasks |
| PUT | /tasks/{id} | Complete task |
| DELETE | /tasks/{id} | Delete task |

## API Documentation
The OpenAPI specification is available in `openapi.yaml`.

## Project Structure
- app.py – Flask backend
- test_app.py – Pytest test cases
- requirements.txt – Dependencies
- openapi.yaml – API documentation
- docs/ – Requirements and ER diagram
- report/ – Final practical report