# TO-DO: Implement a recursive implementation of binary search
import math

#Example 1 

def binary_search(arr, target, start, end):
    # $%$Start
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)

#Example 2

def binary_search(arr, target, start, end):
    if end - start + 1 <= 0:
        return False
    else:
        midpoint = start + (end - start) // 2
        if arr[midpoint] == target:
            return midpoint
        else:
            if target < arr[midpoint]:
                return binary_search(arr, target, start, midpoint -1)
            else:
                return binary_search(arr, target, midpoint + 1, end)

#Example 3

def binary_search(arr, target, start, end):
    if start >= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            return binary_search(arr, target, start, mid -1)
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, start)
        elif arr[mid] == target:
            return mid
    return -1

#This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# def agnostic_binary_search(arr, target):
#     middle = (low + high) //2

#     if len(arr) == 0:
#         return -1 # array emptye


def agnostic_binary_search(arr, target, min=0, max=None):
    if not arr[0] <= target <= arr[-1]:
        return False
    if max is None:
        max = len(arr) -1

    mid - (min + max) // 2

    if arr[mid] == target:
        return mid 
    elif target < arr[mid]:
        max = mid - 1
    elif arr[mid] < target:
        min = mid + 1
    return agnostic_binary_search(arr, target, min, max)

def agnostic_binary_search(arr, target):
    first = 0
    last = len(arr)-1
    found = False
	
    while first<=last and not found:
          midpoint = (first + last)//2
          if arr[midpoint] == target:
                found = True
          else:
              if target < arr[midpoint]:
                    last = midpoint-1
              else:
                    first = midpoint+1
    
    return found