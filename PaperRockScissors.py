import random

list = ["rock", "scissors", "paper"]
dict = {1: "rock", 2: "scissors", 3: "paper"}

chk = True
while chk:
    random_selection = random.choice(list)
    choic = int(input("Enter your choice:\n1. Rock.\n2. Scissors\n3. Paper\n4. Quit\n"))
    if choic not in [1, 2, 3]:
        exit()
    elif dict[choic] == random_selection:
        print("Tie try again")
        print(dict[choic])
        print(random_selection)
    elif dict[choic] == "paper" and random_selection == "rock":
        print("You win!")
        print("You choose " + dict[choic] + " Computer choose " + random_selection)
    elif dict[choic] == "scissors" and random_selection == "paper":
        print("You win!")
        print("You choose " + dict[choic] + " Computer choose " + random_selection)
    elif dict[choic] == "rock" and random_selection == "scissors":
        print("You win!")
        print("You choose " + dict[choic] + " Computer choose " + random_selection)
    else:
        print("You loose!!!")
        print("You choose " + dict[choic] + " Computer choose " + random_selection)
