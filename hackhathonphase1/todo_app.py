from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent

planner = PlannerAgent()
coder = CoderAgent()
tester = TesterAgent()

todos = []

while True:
    print("\n1. Add Todo\n2. List Todos\n3. Complete Todo\n4. Delete Todo\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        coder.create_todo(todos, task)

    elif choice == "2":
        for t in todos:
            status = "✅" if t["completed"] else "❌"
            print(f"{t['id']}. {t['task']} {status}")

    elif choice == "3":
        tid = int(input("Todo ID: "))
        coder.complete_todo(todos, tid)

    elif choice == "4":
        tid = int(input("Todo ID: "))
        todos = coder.delete_todo(todos, tid)

    elif choice == "5":
        break

    tester.validate(todos)
