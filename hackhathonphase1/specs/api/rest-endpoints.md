# REST API Endpoints (Phase II)

## Base URL
- Development: `http://localhost:8000`

## Authentication
All endpoints require a valid JWT token in the HTTP header:

Authorization: Bearer `<token>`

The backend verifies the token using a shared secret (e.g. `BETTER_AUTH_SECRET`) and extracts the `user_id`. The `user_id` in the URL path must match the one in the token, otherwise the request is rejected.

## Endpoints

### GET /api/{user_id}/tasks
List all tasks for the authenticated user.

Response: Array of Task objects.

### POST /api/{user_id}/tasks
Create a new task for the authenticated user.

Request Body:
- `title`: string (required)
- `description`: string (optional)

Response: Created Task object.

### GET /api/{user_id}/tasks/{id}
Get a single task by id for the authenticated user.

Response: Task object if found and owned by the user; 404 otherwise.

### PUT /api/{user_id}/tasks/{id}
Update an existing task owned by the authenticated user.

Request Body:
- `title`: string (optional)
- `description`: string (optional)
- `completed`: boolean (optional)

Response: Updated Task object.

### DELETE /api/{user_id}/tasks/{id}
Delete an existing task owned by the authenticated user.

Response: 204 No Content on success.

### PATCH /api/{user_id}/tasks/{id}/complete
Toggle the completion status of a task.

Response: Updated Task object with `completed` flipped.


