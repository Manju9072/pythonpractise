x, y, z = int(input("Enter First numbers:")), int(input("Enter second numbers:")), int(input("Enter third numbers:"))

if x > y and x > z:
    print("Largest of three is :", x)
elif y > x and y > z:
    print("Largest of three is :", y)
else:
    print("Largest of three is:", z)
print("Three numbers are:", x, y, z)
