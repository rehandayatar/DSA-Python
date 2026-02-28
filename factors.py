# num = 20
# result = []
#
# for i in range(1,num+1):
#     if num % i == 0:
#         result.append(i)
# print(result)

# num = 20
# result = []
# for i in range(1,num//2 + 1):
#     if num % i == 0:
#         result.append(i)
# result.append(num)
# print(result)

from math import sqrt
num = 20
result = []
for i in  range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num // i != 0:
            result.append(num // i)
result.sort()
print(result)
