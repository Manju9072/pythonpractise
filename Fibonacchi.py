def fibo(num, a, b):
    while num > 0:
        a, b = b, a + b
        print(b)
        num = num - 1


num = int(input("Enter a number:\n"))
a, b = 0, 1
print(a)
print(b)

fibo(num, a, b)
