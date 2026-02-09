# Feature: Task CRUD Operations (Phase II Web)

## User Stories
- As an authenticated user, I can create a new task.
- As an authenticated user, I can view all my tasks.
- As an authenticated user, I can update a task.
- As an authenticated user, I can delete a task.
- As an authenticated user, I can mark a task as complete or incomplete.

## Domain Model
- **Task**
  - `id`: integer, auto-increment primary key
  - `user_id`: string, foreign key to auth user id
  - `title`: string, required, 1–200 characters
  - `description`: string, optional, max 1000 characters
  - `completed`: boolean, default false
  - `created_at`: timestamp, default now
  - `updated_at`: timestamp, auto-updated on change

## Acceptance Criteria

### Create Task
- Request is authenticated via JWT.
- Title is required and between 1 and 200 characters.
- Description is optional and at most 1000 characters.
- Task is stored in Neon PostgreSQL and associated with the current user.
- Response returns the created task object.

### View Tasks
- Only tasks for the authenticated `user_id` are returned.
- Response includes `id`, `title`, `description`, `completed`, `created_at`, and `updated_at`.
- Supports listing all tasks without filters in Phase II (filtering/sorting can be added later).

### Update Task
- Only the owner of the task (matching `user_id`) can update it.
- Can update `title`, `description`, and `completed`.
- `updated_at` is refreshed on every update.

### Delete Task
- Only the owner of the task can delete it.
- Deleting a task removes it from the database permanently.

### Mark Complete / Incomplete
- `PATCH /api/{user_id}/tasks/{id}/complete` toggles the `completed` status.
- Only the owner of the task can toggle completion.
- Response returns the updated task object.


