def tictactoeboard(row, col, list):
    print(' ---' * col)
    for e in range(row):

        print("| ", end="")
        for e1 in range(row):
            print((str(list[e][e1])) + " | ", end="")
        print("")

        print(' ---' * col)


def diagnolcheck(list, player):
    flag = 0
    flag1 = [list[ele][ele] for ele in range(len(list[0])) if list[ele][ele] == player]
    flag2 = [list[int(ele)][len(list[0]) - int(ele) - 1] for ele in range(len(list[0])) if
             list[int(ele)][len(list[0]) - int(ele) - 1] == player]
    if len(flag1) == len(list[0]) or len(flag2) == len(list[0]):
        flag = 1
    return flag


def rowcolumn(list, player):
    flag = 0
    row = zip(*list)
    row1 = tuple(row)
    for ro in range(len(tuple(row1))):
        # print(ro)
        if row1[ro].count(player) == len(list[0]):
            flag = 1
            break

    for r in (list):
        if r.count(player) == len(list[0]):
            flag = 1
            break
    return flag
