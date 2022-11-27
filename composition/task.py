"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""


class Profile:
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(f'Name: {self.name}\n'
              f'Lastname: {self.last_name}\n'
              f'Age: {self.age}\n'
              f'passport: {self.passport}')


class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance


class Order:

    def __init__(self):
        self.item = None
        self.date = None
        self.delivery = None
        self.price = None

    def set_all(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price


class User:
    def __init__(self, profile, address, role, bank_account, order):
        self.profile = profile
        self.address = address
        self.role = role
        self.bank_account = bank_account
        self.order = order

    def create_profile(self):
        name = input('Enter name: ')
        last_name = input('Enter lastname: ')
        age = int(input('Enter age: '))
        passport = int(input('Enter passport: '))
        self.profile = Profile(name, last_name, age, passport)
        return self.profile

    def check_info(self):
        while True:
            self.create_profile()
            print('Check your info!')
            self.profile.print_info()
            check = str(input('All correct? yes/no'))
            if check == 'yes':
                break
            else:
                print('Заполните форму заново')
                continue

    def create_address(self):
        city = input('Enter city: ')
        street = input('Enter street: ')
        zipcode = int(input('Enter zipcode: '))
        self.address = Address(city, street, zipcode)

    def create_role(self, role, hours_worked):
        self.role = Role(role, hours_worked)

    def create_bank_account(self, card_number, balance):
        self.bank_account = BankAccount(card_number, balance)

    def create_order(self, item, date, delivery, price):
        self.order = Order()
        self.order.set_all(item, date, delivery, price)


def usr_check():
    user = User(None, None, None, None, None)
    user.check_info()
    user.create_address()
    user.create_role('Accountant', 10)
    user.create_bank_account('34987654', 1000)
    user.create_order('ball', '2022-11-12', 'WB', 12220)

    user.profile.print_info()
    print(user.address.city, user.address.street, user.address.zipcode)
    print(user.role.role, user.role.hours_worked)
    print(user.bank_account.card_number, user.bank_account.balance)
    print(user.order.item, user.order.date, user.order.delivery, user.order.price)


usr_check()