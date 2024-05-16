# Nathaniel Van Woert
# CIS129 Lab 12
# Pet information program

# Design class pet
class Pet:
    def __init__(self, name='', type='', age=0):
        self.name = name
        self.type = type
        self.age = age
    
    # Methods used for main function
    def setName(self, name):
        self.name = name
    
    def setType(self, type):
        self.type = type
    
    def setAge(self, age):
        self.age = age
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getAge(self):
        return self.age

def main():
    # Declare input variables
    inputName = ""
    inputType = ""
    inputAge = 0

    # Create a Pet object
    Animal = Pet()

    # Get values for a pet
    inputName = input("Enter a pet name: ")
    Animal.setName(inputName)

    inputType = input("Enter a pet type: ")
    Animal.setType(inputType)

    inputAge = int(input("Enter a pet age: "))
    Animal.setAge(inputAge)

    # Show values for the pet
    print(f"The pet name is: {Animal.getName()}")
    print(f"The pet type is: {Animal.getType()}")
    print(f"The pet age is: {Animal.getAge()}")

if __name__ == "__main__":
    main()