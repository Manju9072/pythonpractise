import random
import string

dic = {1: 7, 2: 10, 3: 15}
# print(help(string))
characters = string.printable[:-6]
characters_list = list(characters)
# print(characters_list)
choic = int(input("Select password type:\n1. Weak.\n2. Medium.\n3. Strong.\n"))
passwor = []
for char in range(dic[choic]):
    passwor.append(random.choice(characters_list))

password = "".join([char for char in passwor])

print(password)
