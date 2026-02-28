import math

n = 145
num = n
sum_fact = 0

while num > 0:
    ld = num % 10
    sum_fact += math.factorial(ld)
    num //= 10
print(sum_fact)
if sum_fact == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
