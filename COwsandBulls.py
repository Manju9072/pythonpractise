import random

print("Welcome to Cows and bull game!!!\nTo exit press enter two times..")
print("Enter a four digit number:")
num = random.sample(range(0, 9), 4)
lsit_number = num
num = int("".join([str(el) for el in num]))
# print(lsit_number)
# print(num)

state = False


def checkcowsandbulls(usernum):
    num1 = usernum
    cows = bulls = 0
    # bulls = 0
    cn = 1

    while num1 >= 1:
        rem = num1 % 10
        num1 = int(num1 / 10)

        if rem in [int(ele) for ele in set(lsit_number)]:
            # print("cn=", cn)
            if int(lsit_number[-cn]) == rem:
                cows = cows + 1
                # print('in cow', int(lsit_number[-cn]), rem)
            else:

                bulls = bulls + 1
                    # print('in bulls', int(lsit_number[-cn]), rem)
        cn = cn + 1

    # print("in function",cows,bulls,cn)
    return cows, bulls


numberofattempts = 0

try:
    while state == False:
        numberofattempts += 1
        usernum = int(input())
        if usernum >= 10000 or usernum < 1000:
            print("Enter 4 digit number!!!")
        else:

            if (num / usernum) == 1.0:
                if numberofattempts == 1:
                    print('Kudos!!\nYou Guessed in first attempt!!!!')
                    break
                else:
                    print("Bingo 4 cows!!!\nYou Guessed in ", numberofattempts, " Attempts!!")
                    break
            else:
                cow, bull = checkcowsandbulls(usernum)
                print("Cows: ", cow, " Bulls: ", bull)
except Exception as e:
    print("You gave up!!!!!",e)
