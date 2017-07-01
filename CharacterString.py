import time

name = input("May i know your name?")
print("Hi " + name.capitalize() + " Welcome!")
age = int(input("Please enter your age:"))
today = int(time.strftime('%Y', time.localtime()))
print(name.capitalize() + " You are going to turn 100 years on " + str(today + 100 - age))
