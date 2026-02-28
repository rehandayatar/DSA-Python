

# temp = []
# for i in range(0,n):
#     if nums[i] != 0:
#         temp.append(nums[i])
# nz = len(temp)
# for i in range(0,nz):
#     nums[i] = temp[i]
# for i in range(nz,n):
#     nums[i] = 0
#
# print(nums)
nums = [1,3,0,5,0,8,6,8,0]
def moveZeros(nums):

    n = len(nums)
    if len(nums) == 1:
        return
    i = 0
    if i == n:
        return
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    j = i + 1
    while j < n:
        if nums[j] != 0:
            nums[j],nums[i] = nums[i],nums[j]
            i += 1
        j += 1

moveZeros(nums)
print(nums)


