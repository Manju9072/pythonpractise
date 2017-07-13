import random

list = [random.randrange(ele) for ele in range(2, 100)]
print("Original list:")
print(list)

list2 = [ele for ele in list if ele % 2 == 0 and ele != 0]

print("Even numbers in the list:")
print(list2)
print("Unique element:")
print(set(list2))
