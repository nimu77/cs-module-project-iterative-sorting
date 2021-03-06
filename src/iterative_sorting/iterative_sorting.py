# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # for i in range(0, len(arr) - 1):
    #     lhs = i
    #     for j in range(lhs + 1, len(arr)):
    #         if arr[lhs] > arr[j]:
    #             lhs = j

    #     arr[lhs], arr[i] = arr[i], arr[lhs]


    # return arr
    swap_occured = True

    while swap_occured:
        swap_occured = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_occured = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    # loop through for arr
    for value in arr:
        # for each distinct arr value, increment arr[value] by 1
        buckets[value] += 1

    # at this point, our buckets array has all of the counts of
    # every distinct value in our input array

    output = []
    # loop through our buckets array
    for index, count in enumerate(buckets):
        # for the current count
        output.extend([index for i in range(count)])

    return output
