with open("happynumbers.txt", 'r') as happfile, open("primenumbers.txt", 'r') as primefile:
    happy = happfile.readlines()
    prim = primefile.readlines()

if len(happy) < len(prim):
    loop = prim
    sec = happy
else:
    sec = prim
    loop = happy

result = [ele.strip() for ele in loop if ele in sec]

print(result)
