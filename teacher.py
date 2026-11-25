from user import User


class Teacher(User):
    def __init__(self, name: str, surname: str, experience: int):
        super().__init__(name, surname)
        self._experience = experience

    def teach(self) -> None:
        pass
