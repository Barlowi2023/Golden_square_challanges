class TaskTracker:

    def __init__(self):
        self._task_list = []           

    def add_todo(self, todo):
        print(f"the todo: {todo} has been added")
        self._task_list.append(todo)
        return self._task_list

    def list_incomplete(self):
        return self._task_list

    def mark_complete(self, index):
        if index < 0 :
            raise Exception("Error this value is lower than the boundary limit")
        elif index >= len(self._task_list):
            raise Exception("Error this value is greater than the boundary limit")
        else:
            del self._task_list[index]

