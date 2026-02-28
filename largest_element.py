nums = [-1,-2,-3,-670,-69,0,-5,-3]
largest =  float("-inf")
n = len(nums)
for i in range(0,n):
    # if nums[i] > largest:
    #     largest = nums[i]
    largest = max(largest,nums[i])
print(largest)



