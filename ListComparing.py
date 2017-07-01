import random


def randomlist(num):
    list = []
    for i in range(1, num):
        list.append(random.randrange(i))
    return list


list = randomlist(29)
list1 = randomlist(45)
print("First List items:")
print(list)
print("Second List items:")
print(list1)
