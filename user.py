class User:
    _all_users_count = 0

    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        User._all_users_count += 1

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    @classmethod
    def get_all_users_count(cls) -> int:
        return cls._all_users_count
