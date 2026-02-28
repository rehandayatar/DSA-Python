# Using parameterized recursion
# sum = 0
# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
#
# func(sum,1,4)

# Using functional recursion
def func(n):
    if n==1:
        return 1
    return n+func(n-1)

print(func(4))