with open('Training_01.txt', 'r') as fil:
    list = fil.readlines()

print(len(list))
lis = []
tot = 0
for line in list:
    lis.append(line.split('/')[2])
set = set(lis)
for ele in set:
    print(ele, lis.count(ele))
    tot += lis.count(ele)
print(tot)
