n = 1234
num = n
sum = 0
while num>0:
    ld = num % 10
    sum = sum + ld
    num = num // 10
print(sum)

