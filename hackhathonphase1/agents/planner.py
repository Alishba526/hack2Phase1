class PlannerAgent:
    def plan(self):
        return {
            "actions": [
                "add",
                "list",
                "complete",
                "delete",
                "exit"
            ],
            "data_structure": "list of dicts",
            "todo_format": {
                "id": "int",
                "task": "str",
                "completed": "bool"
            }
        }
