# nums = [1,2,3,4,5,6,7,-8]

# PYTHONIC WAY
# nums[:] = [nums[n-1]] + nums[0:n-1]
# nums[:] = [nums.pop()] + nums

# ---------RIGHT ROTATION---------
# temp = nums[n - 1]
# for i in range(n - 1,0,-1):
#     nums[i] = nums[i - 1]
# nums[0] = temp


# temp = nums[n - 1]
# for i in range(n - 2,-1,-1):
#     nums[i + 1] = nums[i]
# nums[0] = temp

# ---------LEFT ROTATION---------
# temp = nums[0]
# for i in range(0 , n - 1):
#     nums[i] = nums[i + 1]
# nums[n - 1] = temp



# USING FUNCTIONS LEFT ROTATION BY ONE
def right_rotate_by_one(nums):
    n = len(nums)
    if n <= 1:
        return

    last = nums[0]          # store last element
    for i in range(0,n - 1):
        nums[i] = nums[i + 1]
    nums[-1] = last

nums = [1,2,3,4,5]
right_rotate_by_one(nums)
print(nums)
