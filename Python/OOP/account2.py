class Account:

    def __init__(self, name):
        self.name = name
        self.balance = 0.00


    def get_name(self):
        return self.name


    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balance += amount


    def get_balance(self):
        return self.balance


    def withdraw(self):
        print('Account withdrawn')


    def deposit(self, amount):
        self.balance += amount


ode = Account('ode')
print(ode.get_balance())
ode.set_balance(100)
print(ode.get_balance())

