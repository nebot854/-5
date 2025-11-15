# Сохраненные пользователи
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
}

print("В системе зарегистрированы следующие пользователи:")
for username, password in users.items():
    print(f"Логин: {username}, Пароль: {password}")

print("\nДобавление нового пользователя.")
username = input("Введите логин нового пользователя: ")
if username in users:
    print("Такой логин уже существует.Ведите пожалуйста другой")


else:
    password = input("Введите пароль нового пользователя: ")
    users[username] = password
    print(f"Новый пользователь {username} успешно добавлен.")

print("\nСписок всех пользователей после добавления нового:")
for username, password in users.items():
    print(f"Логин: {username}, Пароль: {password}")