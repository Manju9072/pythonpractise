from tictactoe import tictactoe1

print("Welcome to tic tac toe!!!!")
row = int(input("Enter the row board size:"))
col = int(input("Enter the column board size:"))
boardvalues = [[0 for ele1 in range(row)] for ele in range(col)]
# print(list1)

tictactoe1.tictactoeboard(row, col, boardvalues)
x = 0
player1, player2 = 'X', 'O'
playrlist = [player1, player2]
while x != 1:
    for player in playrlist:
        userrow, usercolm = int(input("Enter row values:")), int(input("Enter column values:"))

        if boardvalues[userrow - 1][usercolm - 1] == 0:
            boardvalues[userrow - 1][usercolm - 1] = player
            tictactoe1.tictactoeboard(row, col, boardvalues)
        else:
            print("Place already taken!!!")

        x = tictactoe1.diagnolcheck(boardvalues, player)
        if x != 1:
            x = tictactoe1.rowcolumn(boardvalues, player)

        if x == 1:
            print(player, " Player1 won")
            break
        else:
            print("Draw")
