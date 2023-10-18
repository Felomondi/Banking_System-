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

