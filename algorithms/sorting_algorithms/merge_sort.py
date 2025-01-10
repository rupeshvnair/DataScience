# import pdb
# def merge_sort(arr):
#     """
#     Sorts an array using the merge sort algorithm.
#     :param arr: List of elements to be sorted.
#     :return: Sorted list.
#     """
#     if len(arr) <= 1:
#         return arr  # Base case: a single-element list is already sorted
#
#     # Split the array into two halves
#     #pdb.set_trace()
#     middle = len(arr) // 2
#     left_half = merge_sort(arr[:middle])  # Recursively sort the left half
#     right_half = merge_sort(arr[middle:])  # Recursively sort the right half
#
#     # Merge the sorted halves
#     return merge(left_half, right_half)
#
#
# def merge(left, right):
#     """
#     Merges two sorted arrays into a single sorted array.
#     :param left: Sorted left half.
#     :param right: Sorted right half.
#     :return: Merged and sorted array.
#     """
#     #pdb.set_trace()
#     result = []
#     i = j = 0
#
#     # Compare elements from both halves and add the smallest one to the result
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # Add any remaining elements from the left and right halves
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# # Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)
for i,j in enumerate(arr):
    print(f"The index is {i} and the value is {j}")
