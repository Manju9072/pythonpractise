num = int(input("Please enter a number to check if the entered number is even or odd: "))
if (num % 2) == 0:
    if (num % 4) == 0:
        print(num, "is a even number and divisible by 4.")
    else:
        print(num, " is a even number.")
else:
    print(num, " is a odd number.")

div = int(input("Please enter a number to check if it is divides the first number evenly: "))

if (num % div) == 0:
    print(div, "Divides", num, "evenly")
else:
    print(div, "does not divides", num, "evenly")
