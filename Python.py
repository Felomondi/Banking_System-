#Parent Class: User
#. Holds details about the user
#. Has a function to show user details

#Author: Felix Omondi
#Date: 18th October, 2023 

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
    
    def show_details (self):
        print("User Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
# Child Class: Bank
# . Stores details about the account balances
# . Stores details about the amount
# . Allows for deposits, withdraw and view_balance.


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0


     #depositing 
    def deposit (self, amount):
        self.amount = amount 
        self.balance = self.balance + self.amount 
        print("Your Account Balance has been updated!")
        print("Your new account balance is: $", self.balance)

    #withdrawing
    def withdraw (self, amount):
        self.amount = amount 
        if self.amount > self.balance:
            print("Sorry! You have insufficient funds to withdraw the amount")
            print("Your balance is: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("$", self.amount, " was deducted from your account")
            print("Your new balance is: $", self.balance)

    #view_balance
    def view_balance(self):
        self.show_details()
        print("Account Balance: $",self.balance)

