import random
import string
import sys


def art(tries):
    if tries > 1:
        print("______________")
    if tries > 2:
        print("||    !")
    if tries > 3:
        print("||  (o o)")
    if tries > 4:
        print("||    |")
        print("|| /  |  \\")
    if tries > 5:
        print("||  __|__  ")
    if tries > 6:
        print("|| /     \ ")
        print("______________")
        print("You are Hanged!!!")
        print("The word was:{}".format(word))
        sys.exit()


def hangmen():
    alphabetlist = [alp for alp in string.ascii_uppercase]
    list1 = [' _ ' for i in range(len(word))]
    print(len(word))
    print("".join(list1))
    tries = 1
    while True:
        alp = input("Guess an alphabet:")
        if alp.upper() in alphabetlist:
            alphabetlist.remove(alp.upper())
            if alp.upper() in word:

                for i in range(len(word)):

                    if word[i] == alp.upper():
                        list1.pop(i)
                        list1.insert(i, " " + alp.upper())
                        print(list1.count(" _ "))

                print("".join(list1))
            else:

                tries += 1
                art(tries)
                print("\n" + "".join(list1))
                # art(tries)

            if list1.count(' _ ') == 0:
                break
        elif alp.upper().isalpha() is False:
            print("Enter an alphabet")
        else:

            print("Alphabet already selected")


if __name__ == '__main__':
    with open('sowpods.txt', 'r') as filer:
        wordlist = filer.readlines()
    word = random.choice(wordlist).strip()
    # print(word)
    # tkinter._test()
    hangmen()
