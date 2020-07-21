# TO-DO: complete the helper function below to merge 2 sorted arrays
import math

def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []
    while(len(arrA) and len(arrB)):
        if(arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    while(len(arrA)):
        merged_arr.append(arrA.pop(0))
    while(len(arrB)):
        merged_arr.append(arrB.pop(0))
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if(len(arr) < 2):
        return arr
    middle = math.floor(len(arr)/2)
    left = arr[:middle]
    right = arr[middle:]
    arrA = merge_sort(left)
    arrB = merge_sort(right)
    return merge(arrA, arrB)
print(merge_sort([1,3,5,8,6,2,4,7,9]))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
#     # Your code here
# def merge_sort_in_pace(arr, l, r):
#     # Your code here