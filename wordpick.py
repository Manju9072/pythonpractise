import random

with open('sowpods.txt', 'r') as fie:
    x = fie.readlines()
# print(x)
word = random.choice(x)
print(word)
