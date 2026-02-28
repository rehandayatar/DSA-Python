n = 4321
num = n
result = 0
while num>0:
    ld = num % 10
    result = (result*10) + ld
    num = num // 10
print(result)
if result == n:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")

