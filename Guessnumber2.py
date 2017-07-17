def guess_numerr2():
    low = 0
    hig = 100
    cn = 0
    while low <= hig:
        cn = cn + 1
        sum = hig + low
        mid = sum // 2
        print("Is this your Number:", mid)
        flag = int(input("1. Yes.\n2. No.\n"))
        if flag == 2:
            print("Is the number\n")
            choi = int(input("1. Higher\n2. Lower\n"))
            if choi == 1:
                low = mid + 1
            else:
                hig = mid - 1

        else:
            print("I took {} number of guesses!!".format(cn))
            break


guess_numerr2()
