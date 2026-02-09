class CoderAgent:
    def create_todo(self, todos, task):
        todo = {
            "id": len(todos) + 1,
            "task": task,
            "completed": False
        }
        todos.append(todo)

    def complete_todo(self, todos, todo_id):
        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = True

    def delete_todo(self, todos, todo_id):
        return [t for t in todos if t["id"] != todo_id]
