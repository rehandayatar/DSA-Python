n = 1234
num = n
reverse = 0
while num>0:
    ld = num % 10
    reverse = reverse*10 + ld
    num = num // 10
print(reverse)


