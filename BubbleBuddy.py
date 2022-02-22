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

    #print(lst)

    j = startOfList
    for i in lst :
        lst[j] = j
        #print(lst[j])
        j = j + spacing
        
    # end condition?
    lst.append([])
        
    return lst

# Generates a random list of desired length
def creatRandomList(sizeOfList):
    n = sizeOfList
    lst = [[] for _dummy in range(n)]

    #print(lst)
    j = 0
    for i in lst :
        lst[j] = random.randint(0,100)
        j = j + 1
        #print(lst[j])
        
    return lst





# randomList1 = creatList(10, 0, 1)
randomList2 = creatRandomList(10)

#print(randomList1)
print(randomList2)

# endOfList2 = randomList2 [-1]
# print(endOfList2)



# cutList = randomList2[slice(1,len(randomList2))]
# cutList.append([])
# print(cutList)

print(len(randomList2) - 1)
print()

tempList = randomList2

endCond = False
while endCond != True:
    j=len(randomList2) - 1
    k = 0
    for i in randomList2:
        print()
        print(k)
        print(-j)
        print()
        if randomList2[k] > tempList[-j]:
                randomList2[k] = tempList[-j]
        k = k + 1
        j = j - 1
    
    endCond = True

print()
print(randomList2)

