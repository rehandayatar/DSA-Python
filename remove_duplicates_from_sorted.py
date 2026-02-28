nums = [1,2,3,4,4,4,4,5,5,6,6,7,8,9,10]

def check_dup(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    return list(freq_map.keys())
nums = check_dup(nums)
print(nums)


# def check_nums(nums):
#     n = len(nums)
#     if n == 1:
#         return 1
#     i = 0
#     j = i + 1
#     while j < n:
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i],nums[j] = nums[j],nums[i]
#         j += 1
#     return i + 1
# k = check_nums(nums)
# print(k)
# print(nums[:k])

# def check_nums(nums):
#     n = len(nums)
#     if n == 1:
#         return 1
#     i = 0
#     for j in range(1,n):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#
#     return i + 1
# k = check_nums(nums)
# print(nums[:k])