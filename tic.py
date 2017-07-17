def tictactoeboard(size, col):
    for e in range(size):
        print(' ---' * col)
        print(('|' + " " * 3) * (int(col) + 1))

    print(' ---' * col)


print("Welcome to tic tac toe!!!!")

size = int(input("Enter the row board size:"))
col = int(input("Enter the column board size:"))

tictactoeboard(size, col)
