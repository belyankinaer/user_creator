from user import User


class Student(User):
    def __init__(self, name: str, surname: str, student_id: int):
        super().__init__(name, surname)
        self._student_id = student_id

    def learn(self) -> None:
        pass
