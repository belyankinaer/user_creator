from user_factory import UserFactory


def main():
    user1 = UserFactory.create_user("student", "Ваня", "Иванов", 1)
    user2 = UserFactory.create_user("teacher", "Петя", "Петров", 5)
    user3 = UserFactory.create_user("student", "Вася", "Васильков", 2)

    print(f"Total users: {UserFactory.get_all_users_count()}")
    print(f"User1: {user1.get_name()} {user1.get_surname()}")
    print(f"User2: {user2.get_name()} {user2.get_surname()}")
    print(f"User3: {user3.get_name()} {user3.get_surname()}")


if __name__ == "__main__":
    main()
