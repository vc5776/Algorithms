"""
If r > l
    1. Find the middle point to divide the array into two halves:
        middle m = l + (r-l)/2
    2. Call mergeSort for first half:
        Call mergeSort(arr, l, m):
    3. Call mergeSort for second half:
        Call mergeSort(arr, m+1,  r)
    4. merge the two halves sorted in step 2 and 3:
        Call merge(arr, l, m, r)

reference URL
https://www.educative.io/edpresso/merge-sort-in-python
https://stackabuse.com/merge-sort-in-python/
https://www.geeksforgeeks.org/merge-sort/
"""



def mergeSort(arr):
    if len(arr) > 1:
        print(len(arr))
        print(arr ,'u')
        mid = len(arr)//2 # finding the mid of the array
        L = arr[:mid] #Dividing the array element
        print(L, '1')
        R = arr[mid:] #into 2 halves
        print(R, '2')
        mergeSort(L) # Sorting the first half
        mergeSort(R) #Sorting the second half
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                print(L , 'A')
            else:
                arr[k] = R[j]
                j += 1
                print(L , 'B')
            k += 1
            
        #Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(L , 'C')
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(L, 'D')
            
"""                
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end='\n')
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end='\n')
    printList(arr)
"""

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(list)
print(list)
