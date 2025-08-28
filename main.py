# Завдання 1
# Створіть наступні класи:
# CreditCardPayment – атрибути currency
# PayPalPayment – атрибути currency
# CryptoPayment – атрибути currency
# Методи:
# pay(amount) – виводить повідомлення
# CreditCardPayment – оплата карткою {amount}{currency}
# PayPalPayment – оплата PayPal {amount}{currency}
# CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у користувача тип рахунку та потрібні атрибути і повертає об’єкт.
# Створіть декілька рахунків, добавте їх у список та для кожної викличте відповідні методи.

class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Pay with CreditCardPayment: {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Pay with PayPalPayment: {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Pay with CryptoPayment: {amount} {self.currency}")


payments_list = []
def create_payment():
    while True:
        user_choice = int(input("Choose payment method - CreditCardPayment(1), PayPalPayment(2), CryptoPayment(3), exit(4): "))

        if user_choice == 1:
            user_currency = input("Enter currency for pay: ")
            user_amount = float(input("Enter amount of money for pay: "))

            credit_card_payment = CreditCardPayment(user_currency)
            credit_card_payment.pay(user_amount)

            payments_list.append({"method": "CreditCardPayment", "value": user_amount, "currency": user_currency})

        elif user_choice == 2:
            user_currency = input("Enter currency for pay: ")
            user_amount = float(input("Enter amount of money for pay: "))

            pay_pal_payment = PayPalPayment(user_currency)
            pay_pal_payment.pay(user_amount)

            payments_list.append({"method": "PayPalPayment", "value": user_amount, "currency": user_currency})

        elif user_choice == 3:
            user_currency = input("Enter currency for pay: ")
            user_amount = float(input("Enter amount of money for pay: "))

            crypto_payment = CryptoPayment(user_currency)
            crypto_payment.pay(user_amount)

            payments_list.append({"method": "CryptoPayment", "value": user_amount, "currency": user_currency})

        elif user_choice == 4:
            print("Program has been closed")
            break

create_payment()

for payment in payments_list:
    print(f"{payment["method"]}. Value: {payment["value"]} {payment["currency"]}")
