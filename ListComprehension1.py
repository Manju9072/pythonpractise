import random

li = random.sample(range(19), 10)
lis = random.sample(range(29), 18)
print(li)
print(lis)
resl = []
res = [resl.append(ele) for ele in li for ele1 in lis if ele == ele1 and ele not in resl]
print(resl)
