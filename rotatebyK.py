nums = [1,2,3,4,5,6]

# BRUTE FORCE
# n = len(nums)
# k = 3
# rotations = k % n
# for _ in range(0,rotations):
#     e = nums.pop()
#     nums.insert(0,e)
# print(nums)

# USING SLICING
# n = len(nums)
# k = 2
# k = k % n
# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)

# USING REVERSE
n = len(nums)
k = 4
k = k % n
def reverse(nums,left,right):
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n - 1)
print(nums)












# k = 16
# n = len(nums)
# k = k % n
# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)