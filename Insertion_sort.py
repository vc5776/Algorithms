"""
insertion Sort


Insertino sort Algorithm
insertionSort(array)
    mark first element as sorted
    for each unsorted element X
        'extract' the element X
        fot j <- lastSortedIndex down to 0
            if current element j < X
                move sorted element to the right by 1
        break loop and inset X here
end insetionSort

time cimplexity
O(n^2)

refenceURL
:https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/
:https://www.programiz.com/dsa/insertion-sort
"""

def insertion_sort(A, n):
    for i in range(n):
        temp = A[i]
        j = i
        while (j > 0) & (temp < A[j -1]):
            A[j] = A[j-1]
            j = j - 1
        A[j] = temp
        
list = [7, 4, 5, 2]

for i in range(len(list)):
    insertion_sort(list, len(list))
    
print(list)
