import pdb
def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    #pdb.set_trace()
    if len(arr) <= 1:
        return arr # Base case: an array of 0 or 1 elements is already sorted
    pivot = arr[len(arr)//2] # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(arr)
print(sorted_array)