# def quick_sort(arr):
#     # Base case
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]              # choose first element as pivot
#     left = []                   # elements smaller than pivot
#     right = []                  # elements greater than pivot
#     equal = []                  # elements equal to pivot
#
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x > pivot:
#             right.append(x)
#         else:
#             equal.append(x)
#
#     # Recursively sort left and right, then combine
#     return quick_sort(left) + equal + quick_sort(right)
#
#
# # Example
# nums = [4, 3, 2, 1, 8, 7, 5, 6]
# sorted_nums = quick_sort(nums)
# print(sorted_nums)


nums = [1,2,5,7,6,4,3,2,8]
def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i = i + 1
        while nums[j] >= pivot and j >= low+1:
            j = j - 1
        if i < j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    return j

def quick_sort(nums,low,high):
    if low < high:
        pi = partition(nums,low,high)
        quick_sort(nums,low,pi-1)
        quick_sort(nums,pi+1,high)
    return nums

print(quick_sort(nums,0,len(nums)-1))


# def partition(arr, low, high):
#     pivot = arr[high]      # choose last element as pivot
#     i = low - 1            # index of smaller element
#
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]   # swap
#
#     # place pivot at correct position
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
#
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)   # partition index
#
#         # recursively sort left and right parts
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)
#
#
# # Example usage
# nums = [4, 3, 2, 1, 8, 7, 5, 6]
# quick_sort(nums, 0, len(nums) - 1)
# print(nums)
#
