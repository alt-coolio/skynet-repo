# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# def menu():
#     print("Size of list:",
#           "Start of list:",
#           "Size of list:")


# Generates list of desired length and starting point
def creatList(sizeOfList, startOfList, spacing):
    n = sizeOfList
    lst = [[] for _dummy in range(n)]

    # print(lst)
    j = startOfList
    for i in lst:
        lst[j] = j
        # print(lst[j])
        j = j + spacing
    # end condition?
    lst.append([])
    return lst


# Generates a random list of desired length
def creatRandomList(sizeOfList):
    n = sizeOfList
    lst = [[] for _dummy in range(n)]
    # print(lst)
    j = 0
    for i in lst:
        lst[j] = random.randint(0, 100)
        j = j + 1
        # print(lst[j])
    return lst


# randomList1 = creatList(10, 0, 1)
randomList2 = creatRandomList(5)

# print(randomList1)
print(randomList2)

# endOfList2 = randomList2 [-1]
# print(endOfList2)
# cutList=randomList2[slice(1,len(randomList2))]
# cutList.append([])
# print(cutList)

# print(len(randomList2) - 1)
# print()
# tempList = randomList2
# print(max(randomList2))

max_num = max(randomList2)
q = len(randomList2)

# j = len(randomList2) - 1
# k = 0
for i in range(q):

    # print()
    # print(k)
    # print(-j)
    # print()
    for n in range(q - i - 1):
        # print()
        # print(q, i, n)
        if randomList2[n] > randomList2[n+1]:
            temp = randomList2[n]
            randomList2[n] = randomList2[n+1]
            randomList2[n+1] = temp
            # print('switched', randomList2[n], randomList2[n+1])
            # print()
print()
print("Sorted list:", randomList2)
