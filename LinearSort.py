list_UnSorted = [7,1,9,0,2,3,4,2,1,5,6,7,8,0,4,6,9,10]
def LinearSort(list_UnSorted):
    for x  in range(0,len(list_UnSorted),+1):
        for y in range(x,len(list_UnSorted),+1):
            if list_UnSorted[x] > list_UnSorted[y]:
                list_UnSorted[x],list_UnSorted[y] = list_UnSorted[y],list_UnSorted[x]

    return list_UnSorted

list_Sorted = LinearSort(list_UnSorted)
print(list_Sorted)
