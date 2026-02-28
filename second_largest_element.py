nums = [34,21,76,86,-98,0,6,4,9,76,86]
# nums.sort()
# print(nums[-2])

# largest = float("-inf")
# sec_largest = float("-inf")
# n = len(nums)
# for i in range(0,n):
#     largest = max(largest,nums[i])
# for i in range(0,n):
#     if nums[i] > sec_largest and nums[i] != largest:
#         sec_largest = nums[i]
#
# print(sec_largest)

largest = float("-inf")
sec_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    if nums[i] > largest:
        sec_largest = largest
        largest = nums[i]
    elif nums[i] > sec_largest and nums[i] < largest:   # (!= also works)
        sec_largest = nums[i]
print(sec_largest)