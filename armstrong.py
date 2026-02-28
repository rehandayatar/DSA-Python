n = 131
num = n
nod = len(str(n))
total = 0
while num>0:
    ld = num % 10
    total = total + (ld ** nod)
    num = num // 10
print(total)

if total == n:
    print("It is an Armstrong number")
else:
    print("Not an Armstrong number")







