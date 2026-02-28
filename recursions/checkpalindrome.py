# Using Loops
# s = "afifa"
# n = len(s)
# left = 0
# right = n-1
# is_palindrome = True
#
# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1
#
#
# if is_palindrome:
#     print("Yes")
# else:
#     print("False")
#

# Using Recursions
s = [234567]
def check_palindrome(s,left,right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s,left+1,right-1)
print(check_palindrome(s,0,len(s)-1 ))

