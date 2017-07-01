list = [1, 2, 3, 5, 1, 3, 8, 12, 32, 19, 9, 7, 45, 32, 321]
list2 = []
[list2.append(itm) for itm in list if itm < 5]
print(list2)
num = int(input("Enter a number to chcek if the list contains numbers less than entered number: "))
list3 = []
[list3.append(itm) for itm in list if itm < num]
print(list3)
