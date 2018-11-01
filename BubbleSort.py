list_UnSorted = [7,1,9,0,2,3,4,2,1,5,6,7,8,0,4,6,9,10]
def BubbleSort(list_UnSorted):
    y = 0
    for y in range(0,len(list_UnSorted)-y,+1):
        for n in range(0,len(list_UnSorted),+1):
            if list_UnSorted[n] > list_UnSorted[y]:
                list_UnSorted[n],list_UnSorted[y] = list_UnSorted[y],list_UnSorted[n]
    return list_UnSorted

list_Sorted = BubbleSort(list_UnSorted)
print(list_Sorted)
