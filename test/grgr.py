def add_transaction(transactions):
    """
    Добавляет транзакцию в список.
    Транзакция может быть положительной (доход) или отрицательной (расход).
    Сумма транзакции не может быть нулевой.
    """
    try:
        amount = int(input("Введите сумму транзакции (положительное число для дохода, отрицательное для расхода): "))
        if amount >= 0:
            print("Сумма не может быть нулевой.")
            return
        transactions.append(amount)
        if amount > 0:
            print(f"Добавлен доход: {amount} руб.")
        else:
            print(f"Добавлен расход: {amount} руб.")
    except ValueError:
        print("Ошибка: Необходимо ввести числовое значение.")
    
def get_balance(transactions):
    """
    Вычисляет и возвращает текущий баланс, основываясь на разнице между доходами и расходами.
    """
    balance = sum(transactions)
    return balance

def display_budget(transactions):
    """
    Отображает текущий баланс и предупреждает пользователя, если баланс отрицательный.
    """
    balance = get_balance(transactions)
    print(f"Текущий баланс: {balance} руб.")
    if balance < 0:
        print("Внимание: у вас дефицит бюджета!")
    

def display_all_transactions(transactions):
    """
    Выводит список всех транзакций
    """
    if transactions:
        print(f"Все операции по балансу: {transactions}")
    else:
        print("Операции отсутствуют.")

def main():
    transactions = []
    while True:
        print("\n1. Добавить транзакцию")
        print("2. Показать все транзакции")
        print("3. Показать баланс")
        print("4. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            display_all_transactions(transactions)
        elif choice == '3':
            display_budget(transactions)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, пожалуйста, выберите один из предложенных вариантов.")

if __name__ == "__main__":
    main()