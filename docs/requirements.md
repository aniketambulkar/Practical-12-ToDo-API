# Software Requirement Specification

The To-Do List REST API will be developed using Python Flask to help users manage tasks through JSON-based HTTP requests. Users can create a task with a title and description, view all tasks, mark a task as completed using its ID, and delete a task using its ID. Each task will have a unique `id`, a `title`, a `description`, and a Boolean `completed` status. The API will validate requests and return appropriate responses for successful operations, invalid input, and tasks that cannot be found.

## User Stories and Acceptance Criteria

### 1. Add a task
**User story:** As a user, I want to add a task with a title and description so that I can keep track of work to do.

- **Given** a valid title and description, **When** I submit a request to create a task, **Then** the API creates a task with a unique ID and `completed` set to `false`.
- **Given** the title is missing, **When** I submit a request to create a task, **Then** the API returns a validation error and does not create the task.

### 2. View all tasks
**User story:** As a user, I want to view all tasks so that I can see what needs to be done and what is complete.

- **Given** tasks exist, **When** I request the task list, **Then** the API returns each task with its ID, title, description, and Boolean completion status.
- **Given** no tasks exist, **When** I request the task list, **Then** the API returns an empty list.

### 3. Mark a task as completed
**User story:** As a user, I want to mark a task as completed using its ID so that I can track my progress.

- **Given** a task exists, **When** I request to complete it using its ID, **Then** the API sets its `completed` status to `true`.
- **Given** no task exists with the specified ID, **When** I request to complete it, **Then** the API returns a not-found response.

### 4. Delete a task
**User story:** As a user, I want to delete a task using its ID so that I can remove tasks I no longer need.

- **Given** a task exists, **When** I request to delete it using its ID, **Then** the API removes the task and confirms the deletion.
- **Given** no task exists with the specified ID, **When** I request to delete it, **Then** the API returns a not-found response.

## Functional Requirements

- **FR1:** The API shall create tasks from a title and description.
- **FR2:** Each task shall include a unique ID, title, description, and Boolean `completed` value.
- **FR3:** New tasks shall have `completed` set to `false`.
- **FR4:** The API shall return all tasks and their fields.
- **FR5:** The API shall set a task’s `completed` value to `true` when requested by ID.
- **FR6:** The API shall delete a task when requested by ID.
- **FR7:** The API shall report invalid input and unknown task IDs with appropriate error responses.
- **FR8:** The API shall use JSON for request and response data.

## Non-Functional Requirements

- **NFR1:** The API shall be implemented using Python Flask.
- **NFR2:** The API shall follow REST conventions and use appropriate HTTP methods and status codes.
- **NFR3:** Responses and error messages shall be clear and consistent.
- **NFR4:** The application code shall be readable and maintainable.
- **NFR5:** The API shall be testable using standard HTTP clients.