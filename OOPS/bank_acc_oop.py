class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance          # encapsulated 

    def deposit(self, amount):
        self.__balance += amount
        print(f" Deposited ₹{amount} | New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount} | New Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):        # inheritance
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate




acc = SavingsAccount("Aarav", 1000)
print(f"Owner: {acc.owner}\n")

acc.deposit(500)
acc.withdraw(200)
