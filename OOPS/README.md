# Python OOP: Bank Account System 🏦

A simple, beginner-friendly Python project demonstrating the core concepts of **Object-Oriented Programming (OOP)**. 

This project models a real-world banking scenario using classes, objects, inheritance, and encapsulation.

## 🧠 OOP Concepts Covered

*   **Encapsulation:** The account balance is protected using a private attribute (`self.__balance`), meaning it can only be modified safely through methods like `deposit()` and `withdraw()`.
*   **Inheritance:** The `SavingsAccount` class inherits properties and methods from the parent `BankAccount` class, reducing code duplication.
*   **Abstraction:** Complex logic (like checking for sufficient funds before a withdrawal) is hidden behind simple method calls.
*   **Classes & Objects:** The blueprint (`BankAccount`) and the actual instance created in memory (`acc`).

## 🚀 Features

*   Create a bank account with an owner name and optional initial balance.
*   Deposit money securely.
*   Withdraw money with built-in insufficient funds validation.
*   Check current balance.
*   Specialized `SavingsAccount` class with an interest rate attribute.

## 💻 Code Overview

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Encapsulated (private)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount} | New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount} | New Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

# --- Demo Execution ---
if __name__ == "__main__":
    acc = SavingsAccount("Aarav", 1000)
    print(f"Owner: {acc.owner}\n")
    
    acc.deposit(500)
    acc.withdraw(200)