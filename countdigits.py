# n = 5678
# num = n
# count = 0
# while num>0:
#     count += 1
#     num = num // 10
#
#
# print(count)



# def count_digits(n):
#     num = n
#     count = 0
#     while num>0:
#         count += 1
#         num = num // 10
#     return count
# print(count_digits(23453442))


from math import *
def count_digits(num):
    if num == 0:
        return 1
    else:
        return log10(num)+1
print(count_digits(000000))
