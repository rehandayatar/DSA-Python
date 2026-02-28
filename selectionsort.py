# ASCENDING ORDER
# nums = [9,8,7,6,5,4,3,2,1]
# def selection_sort(nums):
#     n = len(nums)
#     for i in range(0,n):
#         min_index = i
#         for j in range(i+1,n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i],nums[min_index] = nums[min_index],nums[i]
#     return nums
#
#
# print(selection_sort(nums))

# DESCENDING ORDER
nums = [1,2,3,4,5,6,7,8,9]
def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        max_index = i
        for j in range(1+1,n):
            if nums[j]>nums[max_index]:
                max_index = j
        nums[i],nums[max_index] = nums[max_index],nums[i]


selection_sort(nums)
print(nums)