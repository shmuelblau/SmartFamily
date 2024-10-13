class Task:
    def __init__(self, id: int, user_id: int, task_name: str, description: str, category: int, status: bool = False):
        self.id = id
        self.user_id = user_id
        self.task_name = task_name
        self.description = description
        self.category = category
        self.status = status

    def __repr__(self) -> str:
        return f'\n\
id: {self.id},\
 user id: {self.user_id},\
 task name: {self.task_name},\
 category: {self.category},\
 status: {self.status}\n'
