def calculate():
    print("Введите два числа и выберите операцию.")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == '+':
        print(f"Результат: {num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"Результат: {num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"Результат: {num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        print(f"Результат: {num1} / {num2} = {num1 / num2}")

    else:
        print("Неизвестная операция.")

calculate()