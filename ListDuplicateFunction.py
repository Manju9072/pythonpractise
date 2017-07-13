import random


def set_function(originallist):
    return set(originallist)


def normal_loop_function(original_list):
    removed = []
    for i in original_list:
        if i in removed:
            pass
        else:
            removed.append(i)
    return removed


list = [random.randrange(i) for i in range(2, 200, 4)]
list1 = set_function(list)
list2 = [ele for ele in list1]
# list2=list(list1)
print(list2)
print("-------------------------------------------")
print(sorted(normal_loop_function(list)))
