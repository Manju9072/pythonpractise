num = int(input("Enter a number: "))
divisor_list = []
[divisor_list.append(divisor) for divisor in range(1, (num // 2 + 1)) if num % divisor == 0]
print(divisor_list)

if len(divisor_list) == 1:
    print(num, "Entered Number is a prim number.")
else:
    print(num, "is not a prime number.")
