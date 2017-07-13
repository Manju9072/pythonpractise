import random

list = [random.randrange(rn) for rn in range(10, 100)]
print(list)
list2 = list[:1]
list2.append(list[-1])
print(list2)
