"""
bubble_sort 
repeatedly comparing pairs of adjacent element and then swapping their positions if
they exist in ther wrong order.

1 step
 7 is comparing with 4. Since 7 > 4, 7 is moved ahead of 4. Since all the other 
 elements are of a lesser value than ,  is moved to the end of the array.
 
 [4, 5, 2, 7]
 
2 step
 4 is comparing with 5. Since 5 > 4, not swapping. And  5 is comparing with 2. Since 
 5 > 2, swapping.
 
 [4, 2, 5, 7]
 
3 step
 4 is comparing with 2. Since 4 > 2, swapping.
 
Reference URL
:https://www.geeksforgeeks.org/python-program-for-bubble-sort/
 
"""


def bubble_sort(A, n):
    for k in range(n-1):
        for i in range(n-k-1):
            if(A[ i ] > A[ i + 1]):
                temp = A[i]
                A[i] = A[i+1]
                A[i + 1] = temp
                
list = [7, 4, 5, 2]


for l in range(len(list)):
    bubble_sort(list, len(list))
    
print(list)
