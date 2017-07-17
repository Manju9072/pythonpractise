row1 = [["w" + str(num) for num in range(1, 9)]]
# print(row1)
row2 = [["w" + str(9) for num in range(1, 9)]]
# print(row2)
row7 = [["b" + str(9) for num in range(1, 9)]]
# print(row7)
row3to6 = [["e" + str(0) for num in range(1, 9)]] * 4
# print(row3to6)
row8 = [["b" + str(num) for num in range(1, 9)]]
# print(row8)




row1.extend(row2)
row1.extend(row3to6)
row1.extend(row7)
row1.extend(row8)
for row in row1:
    print(row)

# def elephant():
