import random

print("Welcome to Guess Number!!!!\nType exit to quit!\n")
number = int(random.randint(1, 9))
number_of_times = 1
correctguess = 0
chk = True
while chk:
    print("Round %s guess number %s" % (number_of_times, correctguess))

    num = input("Guess a number between 1 and 9:\n")
    try:
        if num == "exit":
            exit()
        elif int(num) < number:
            print("Guess Higher!!")
            correctguess += 1
        elif int(num) > number:
            print("Guess Lower!!")
            correctguess += 1
        elif int(num) == number:
            correctguess += 1
            print("Bingo you guessed right in %s steps!!" % correctguess)
            number_of_times += 1
            correctguess = 0
    except Exception as e:
        print("Enter valid input!!!")
