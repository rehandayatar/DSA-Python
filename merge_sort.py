# Merge
# left = [1,2,3,4]
# right = [4,4,4,5,6,7,8,9]
# result = []
# def merge(left,right):
#     result = []
#     i,j = 0,0
#     n,m = len(left),len(right)
#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     while i < n:
#         result.append(left[i])
#         i += 1
#     while j < m:
#         result.append(right[j])
#         j += 1
#     return result
# result = merge(left,right)
# print(result)



def merge(left, right):
    """Merge two sorted lists into one sorted list"""
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    # Merge elements while both lists have elements
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    while i < n:
        result.append(left[i])
        i += 1
    while j < m:
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    """Recursively split and sort the array"""
    if len(arr) <= 1:
        return arr  # Already sorted

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half

    return merge(left, right)      # Merge sorted halves


# Example usage
nums = [4, 3, 2, 1, 8, 7, 5, 6]
sorted_nums = merge_sort(nums)
print(sorted_nums)
