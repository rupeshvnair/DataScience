'''
Binary search is a highly efficient algorithm for finding the position of a target element in a sorted array or list.
It works by repeatedly dividing the search interval in half and comparing the target value to the middle element of the interval.
If the target matches the middle element, the search is successful.
Otherwise, the search continues in the left or right half, depending on whether the target is smaller or larger than the middle element.
'''


def binary_searcher(arr,target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid -1
    return -1

arr = [1,3,5,7,9,11]
target = 7
