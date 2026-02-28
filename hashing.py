# n = [1,2,4,5,6,111,234]
# m = [1,2,3,4,5,6,111,234]
# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             count += 1
#
#     print(num,"occurs",count,"times")


# n = [1,2,3,4,5,6]
# m = [1,2,3,4,5]
# for num in m:
#     print(num,"occurs",n.count(num),"times")

n = [1, 2, 4, 5, 6]
m = [1, 2, 7, 5]

freq = {}
for x in n:
    freq[x] = freq.get(x, 0) + 1

for num in m:
    print(num, "occurs", freq.get(num, 0), "times")


