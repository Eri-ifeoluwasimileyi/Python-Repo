class Account:

    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self.balance = balance


    def withdraw(self):
        print('Account withdrawn')


    def deposit(self, amount):
        self.balance += amount



ode = Account('ode', 500000)
print(ode.balance)
ode.deposit(1500)
print(ode.balance)

