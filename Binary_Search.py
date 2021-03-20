"""
First add high value and low value. And divide by 2. So midium value the remains.

Second compared midium value and search value.
If corrent midium value and search value 
  break
else if search value < midium value 
  Add low value and midium value. And divide by 2. So other miduum value the remains.
  And compared midum value and serch value.

else if search value > midium value 
  Add high value and midium value. And divide by 2. So other miduum value the remains.
  And compared midum value and serch value.

Reference
URL : https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/
URL : https://rosettacode.org/wiki/Binary_search#Python

"""

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1
    
line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value = 8

print(binary_search(line, 8))
print(list[(binary_search(line, 8))])




