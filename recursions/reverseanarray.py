# Two-pointer swap (in-place reverse)
nums = [1,2,3,4,5,6,7,8,9]
def reverse(nums,left,right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    reverse(nums,left+1,right-1)
reverse(nums,0,8)
print(nums)


# # Build a new reversed array
# arr = [10, 20, 30, 40, 50]
# rev = []
#
# i = len(arr) - 1
# while i >= 0:
#     rev.append(arr[i])
#     i -= 1
#     print(rev)


# # Using index from start but negative indexing
# arr = [10, 20, 30, 40, 50]
#
# i = 1
# while i <= len(arr):
#     print(arr[-i], end=" ")
#     i += 1
