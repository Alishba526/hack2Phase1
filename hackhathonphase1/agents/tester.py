class TesterAgent:
    def validate(self, todos):
        assert isinstance(todos, list)
        for todo in todos:
            assert "id" in todo
            assert "task" in todo
            assert "completed" in todo
