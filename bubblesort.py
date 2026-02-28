nums = [9,8,7,6,5,4,3,2,1]
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

bubble_sort(nums)
print(nums)

# nums = [9,8,7,6,5,4,3,2,1]
# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             if nums[j] > nums[j + 1]:  # swap if current > next
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums
# print(bubble_sort(nums))

# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(0,n):
#         is_swap = False
#         for j in range(0,n-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 is_swap = True
#         if is_swap == False:
#             break
#     return nums
#
#
# print(bubble_sort(nums))