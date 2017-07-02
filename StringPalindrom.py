string = input("Enter a string to check if it is palidrome or not:")

if string[:int(len(string) / 2)] == string[-int(len(string) / 2):][::-1]:
    print(string + " is a palindrome")
else:
    print(string + " Not a palidrome")
