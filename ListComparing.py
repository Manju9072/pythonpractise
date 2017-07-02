import random


# one way of generating random number it
def randomlist(num):
    """Generate random number using random module."""
    list = []
    for i in range(1, num):
        list.append(random.randrange(i))
    return list


def compair_two_list_using_sets_comman(listone, listtwo):
    return set(listone).intersection(set(listtwo))


def compair_two_list_using_sets_difference(listone, listtwo):
    return set(listtwo).difference(set(listone))


# python way of generating random numbers
li = [random.randrange(itm) for itm in range(1, 30)]
lis = [random.randrange(itm) for itm in range(1, 45)]
print("First list python way:")
print(li)
print("Second list python way:")
print(lis)
print("--------------------------------------------------------------------------")
print("Fastest way to compair list and find comman elements:")
res = compair_two_list_using_sets_comman(li, lis)
print(res)
print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")
print("Fastest way to compair list and find difference between second and first(present in second list not first):")
res = compair_two_list_using_sets_difference(li, lis)
print(res)
print("--------------------------------------------------------------------------")
print("Fastest way to compair list and find difference between first and second(present in first list not second):")
res = compair_two_list_using_sets_difference(lis, li)
print(res)
print("--------------------------------------------------------------------------")


# normal way using single for and in .
def comparing_list_the_old_way(list1, list2):
    res = []
    for ele in list1:
        if ele in list2:
            if ele in res:  # to get unique value.
                pass
            else:
                res.append(ele)
    return res


def comparing_list_the_old_way2(list1, list2):
    result = []
    for ele in list1:
        for ele1 in list2:
            if ele == ele1:
                if ele in result:  # to get unique value.
                    pass
                else:
                    result.append(ele)
    return result


list = randomlist(29)
list1 = randomlist(45)
print("First List items normal way:")
print(list)
print("Second List items normal way:")
print(list1)
res = comparing_list_the_old_way(li, lis)
result = comparing_list_the_old_way2(li, lis)
print("--------------------------------------------------------------------------")
print("Compairing  list the old way 1:")

print(res)
print("--------------------------------------------------------------------------")

print("--------------------------------------------------------------------------")
print("Compairing  list the old way 2:")

print(result)
print("--------------------------------------------------------------------------")
