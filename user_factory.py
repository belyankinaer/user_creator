from student import Student
from teacher import Teacher


class UserFactory:
    _all_users_count = 0

    @classmethod
    def create_user(cls, role: str, *args, **kwargs):
        if role == "student":
            user = Student(*args, **kwargs)
        elif role == "teacher":
            user = Teacher(*args, **kwargs)
        else:
            raise ValueError(f"Unknown role: {role}")

        cls._all_users_count += 1
        return user

    @classmethod
    def get_all_users_count(cls) -> int:
        return cls._all_users_count
