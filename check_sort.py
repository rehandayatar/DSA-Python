nums = [1,2,3,4,5,69]
def check_sort(nums):
    ascending = True
    descending = True
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            ascending = False
        elif nums[i] < nums[i + 1]:
            descending = False
    if ascending:
        print("Ascending")
    elif descending:
        print("Descending")
    else:
        print("Not sorted")


check_sort(nums)


