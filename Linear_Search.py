"""
Linear Search

Every item is checked and if a match is found then that particular item is returned, 
otherwise the search continues till the end of the data collection.

pseudo code example

for (start to end of array)
{
    if (cerrent_element equals to n)
    {
        print (current_index)
    }
}

reference
URL : https://www.hackerearth.com/practice/algorithms/searching/linear-search/tutorial/
URL : https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm
"""

list = [1, 3, 5, 7, 9, 11]

for i in range(len(list)): 
    if list[i] == 9:
        print(list[i])
