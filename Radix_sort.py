"""
Radix sort

Algorithms
radixSort(array)
    d <- maximum number of digits in the largest element
    create d buckets of size 0-9
    for i <- 0 to d
        sort the element according to ith place digits using countingSort
        
countingSort(array, d)
    max <- find largest element among dth place element
    initialize count array with all zeros
    for j <- 0 to size
        find the total count of each unique digit in dth place of element and
        store the count at jth index in count arry
    for i <- 1 to max
        find the cumulative sum and store it in count array itself
    for j <- size down to 1
        restore the element to array
        decrease count of each element restored by 1

Time Complexity
O(d(n+k)).

Reference URL
: https://www.programiz.com/dsa/radix-sort
: https://www.geeksforgeeks.org/radix-sort/
: https://www.hackerearth.com/practice/algorithms/sorting/radix-sort/tutorial/

"""

def countingSort(arr, exp1):
    n = len(arr)   # list lenge
    
    output = [0] * (n)     # list lenge same the list space
    
    count = [0] * (10)     # number count list
    
    for i in range(0, n):    # Add the number count list
        index = (arr[i] / exp1)     
        count[int(index % 10)] += 1
        
    for i in range(1, 10):      # Same the count sort a way. First only number one's space
                                # Second only number ten's space
                                # finally only number hundred space
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:      #Current number space sort
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(arr)):    # arr = output
        arr[i] = output[i]
        
def radixSort(arr):
    max1 = max(arr)    #list max number
    
    exp = 1
    while max1 / exp > 0:  #number space count
        countingSort(arr, exp)
        exp *= 10
        
arr = [170, 45, 75, 90, 802, 24, 2, 66] 

radixSort(arr)


print(arr)
#for i in range(len(arr)):
#    print(arr[i])
