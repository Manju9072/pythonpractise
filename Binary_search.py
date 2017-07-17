'''Non python way'''
listofelements = []


def linear_search(listofelements, userele):
    flg = 0
    for el in listofelements:
        if el == userele:
            flg = 1
            break

    return flg, listofelements.index(el)


def binary_search(listofelements, ele):
    hig = len(listofelements)
    low = 0
    f = 0
    while low <= hig:

        mid = (low + hig) // 2
        if mid >= hig:
            return f
        print(mid, low, hig)
        if listofelements[mid] == ele:
            f = 1
            break
        elif listofelements[mid] < ele:
            low = mid + 1
        else:
            hig = mid - 1
        print(mid)
    return f


listofelements = [1, 2, 5, 4, 7, 8]
userele = int(input("eneter a n element to search:"))
# flag, index = linear_search(listofelements, userele)
flag = binary_search(listofelements, userele)
if flag == 1:
    print("Found at index:")
else:
    print("No element found")
