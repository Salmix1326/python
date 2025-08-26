# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
# ім'я клієнта
# баланс
# валюта
# словник з курсом валют(однаковий для всіх)
# Додайте методи:
# вивід загальної інформації
# перевірка чи відома валюта(якщо ні, викликати ValueError)
# перевести гроші з однієї валюти в іншу(ця операція часто використовується, тому зрочно реалізувати окремим методом)
# зміна валюти
# поповнення балансу(валюта та сама)
# зняття грошей з балансу(валюта та сама).
from copy import deepcopy


exchange_list_for_admin = {"UAH": 1, "USD": 0.024, "JPY": 3.53}

class BankAccount:
    def __init__(self, customer_name, current_currency, current_balance, currency_list, exchange_list):
        self.customer_name = customer_name
        self.current_currency = current_currency
        self.current_balance = current_balance
        self.currency_list = currency_list
        self.exchange_list = exchange_list
        self.old_exchange_list = {}

    def show_account_info(self):
        print("-----Account information-----")

        print(f"Account Name: {self.customer_name}")
        print(f"Account Balance For Active Currency - {self.current_currency}: {self.current_balance}")
        print("")

        print("-----Your Account Currencies----")

        for key, value in self.currency_list.items():
            print(f"Currency Name: {key}. Value: {value}")

        print("--------------------------------")

    def check_currency_type(self, currency_type):
        try:
            if currency_type in self.exchange_list:
                print("We support this currency")

            else:
                raise ValueError("Unsupported currency")

        except ValueError:
            print("We dont support this currency")

    def change_active_currency(self, new_active_currency):
        if new_active_currency not in self.exchange_list:
            print(f"{new_active_currency} is not in exchange list")
            return

        if new_active_currency not in self.currency_list:
            print(f"{new_active_currency} is not in your currencies")
            return

        self.current_currency = new_active_currency
        self.current_balance = self.currency_list[new_active_currency]
        self.old_exchange_list = deepcopy(self.exchange_list)

        base_currency_value = self.old_exchange_list[new_active_currency]

        for key, value in self.old_exchange_list.items():
            self.exchange_list[key] = value / base_currency_value

        print(f"Active currency is successfully changed. Current active currency: {new_active_currency}")

    def exchange_currency(self, currency_type, currency_count, new_currency_type):
            if currency_type not in self.currency_list:
                print(f"{currency_type} is not in your currencies")
                return

            if new_currency_type not in self.currency_list:
                print(f"{new_currency_type} is not in your currencies")
                return

            if currency_type not in self.exchange_list:
                print(f"{currency_type} is not in our exchange list")
                return

            if new_currency_type not in self.exchange_list:
                print(f"{new_currency_type} is not in our exchange list")
                return

            if currency_count > self.current_balance:
                print(f"Your active currency balance is lower than you want to exchange")
                return

            if currency_count < 0:
                print(f"Enter value grater than 0")
                return

            if new_currency_type == self.current_currency:
                print(f"Choose other currency to exchange")
                return

            new_value = currency_count * self.exchange_list[new_currency_type]

            self.currency_list[new_currency_type] += new_value
            self.currency_list[currency_type] -= currency_count
            self.current_balance -= currency_count

            print(f"{currency_count} {currency_type} is successfully exchanged to {new_value} {new_currency_type}")

    def add_active_currency_balance(self, new_value):
        if new_value > 0:
            self.currency_list[self.current_currency] += new_value
            self.current_balance += new_value
            print(f"Balance of active currency {self.current_currency} is successfully increased")
        else:
            print("Enter valid value greater than 0")

    def withdraw_money_from_active_balance(self, value):
        if self.current_balance < value:
            print("Active balance is lower than you want to withdraw")
            return

        if value < 0:
            print("Invalid value. Enter value greater than 0")
            return

        self.current_balance -= value
        self.currency_list[self.current_currency] -= value

        print(f"Withdraw has been successful. Your active balance of currency {self.current_currency} - {self.current_balance}")

    def add_new_currency(self, new_currency):
        if new_currency in self.exchange_list:
            self.currency_list[new_currency] = 0
            print(f"Currency {new_currency} is added to your account")
            print("")

        else:
            print("This currency is not in exchange list")
            print("")

    def delete_currency_from_account(self, currency):
        if currency not in self.currency_list:
            print("This currency is not in your account")
            return

        if self.currency_list[currency] > 0:
            print("You want to delete currency with balance. Choose other currency to exchange or withdraw all balance")
            print("")
            return

        if self.current_currency == "UAH" or currency == "UAH":
            print("You cant delete currency UAH")
            print("")
            return

        self.currency_list.pop(currency)
        print(f"Currency {currency} is deleted from your account")
        print("")

        self.current_currency = "UAH"
        self.current_balance = self.currency_list["UAH"]


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_new_currency_to_exchange_list(self, new_currency, exchange_rate, exchange_list):
        if self.name == "admin1" and self.password == 1111:
            exchange_list[new_currency] = exchange_rate
            print(f"New currency {new_currency} is added to exchange list with rate {exchange_rate}")

    def delete_currency_fron_exchange_rate(self, currency, exchange_list):
        if currency == "UAH":
            print("You cant delete currency UAH")
            return

        if self.name == "admin1" and self.password == 1111:
            exchange_list.pop(currency)
            print(f"Currency {currency} is deleted from exchange list")


admin = Admin("admin1", 1111)

while True:
    admin_choice = int(input("Choose function: add currency or edit exchange rate(1), delete currency(2), exit(3): "))

    if admin_choice == 1:
        admin_currency = input("Enter currency type to add: ")
        admin_exchange_rate = float(input("Enter exchange rate: "))
        admin.add_new_currency_to_exchange_list(admin_currency, admin_exchange_rate, exchange_list_for_admin)

    elif admin_choice == 2:
        admin_currency = input("Enter currency type to delete: ")
        admin.add_new_currency_to_exchange_list(admin_currency, exchange_list_for_admin)

    elif admin_choice == 3:
        break

account1 = BankAccount("Account1", "UAH", 2000,
                       {"UAH": 2000, "USD": 100}, exchange_list_for_admin)

while True:
    try:
        user_choice = int(input(f"Choose service:\nshow account info(1)\ncheck supported currency(2)\n"
                                f"change active currency ({account1.current_currency})(3)\n"
                                f"exchange active currency ({account1.current_currency})(4)\n"
                                f"add money to active currency ({account1.current_currency})(5)\n"
                                f"withdraw money from active balance in active currency({account1.current_currency})(6)\n"
                                f"add new currency to account(7)\n"
                                f"delete currency from account(8)\n"
                                f"exit(9): "))
        print("")

        if user_choice == 1:
            account1.show_account_info()
            print("")

        elif user_choice == 2:
            user_currency = input("Enter currency type: ").upper().strip()
            account1.check_currency_type(user_currency)
            print("")

        elif user_choice == 3:
            user_currency_choice = input("Enter currency type: ").upper().strip()
            account1.change_active_currency(user_currency_choice)
            print("")

        elif user_choice == 4:
            try:
                user_current_currency = account1.current_currency

                user_currency_count_for_exchange = int(input("Enter currency value for exchange: "))
                user_new_currency_type = input("Enter new currency: ").upper().strip()

                account1.exchange_currency(user_current_currency, user_currency_count_for_exchange,
                                           user_new_currency_type)
                print("")

            except ValueError:
                print("Enter valid value")
                print("")


        elif user_choice == 5:
            try:
                user_value = float(input("Enter money value to add to balance: "))
                account1.add_active_currency_balance(user_value)
                print("")

            except ValueError:
                print("Enter valid value")
                print("")

        elif user_choice == 6:
            try:
                user_value = float(input("Enter money value to withdraw: "))
                account1.withdraw_money_from_active_balance(user_value)
                print("")

            except ValueError:
                print("Enter valid value")
                print("")

        elif user_choice == 7:
            try:
                user_currency = input("Enter currency name to add: ").upper().strip()
                account1.add_new_currency(user_currency)

            except ValueError:
                print("Enter valid value")
                print("")

        elif user_choice == 8:
            user_currency = input("Enter currency type: ").upper().strip()
            account1.delete_currency_from_account(user_currency)

        elif user_choice == 9:
            print("Program is closing...")
            print("Program is closed")
            break

    except ValueError:
        print("Enter valid value 1-9")
