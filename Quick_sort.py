"""
QuickSort

QuickSort is a Divide and Conquer algorithm.
1. random value define of pivot.
2. partition
3. reapeat

Refurence URL
:https://www.geeksforgeeks.org/quick-sort/
:https://www.geeksforgeeks.org/python-program-for-quicksort/
"""


def partition(arr, low, high):
    i = (low - 1)   #smaller element
    pivot = arr[high]   #pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]    # swap
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i+1)
    
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    


list = [43, 55, 22, 13, 67, 7, 1]

quickSort(list, 0, len(list)-1)
print(list)
