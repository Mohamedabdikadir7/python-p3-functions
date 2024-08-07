#!/usr/bin/env python3
# function greetProgrammer() {
#   console.log("Hello, programmer!");
# }
def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

 


# def greet(name):
#     print(f"Hello",{name})
# greet("GUIDO")
def greet(name):
    print(f"Hello, {name}!")

greet("Guido")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("ali")

def add(num1, num2):
    return num1 + num2

result = add(45, 55)
print(result)


def halve(number):
    return number / 2

result = halve(8)
print(result)



