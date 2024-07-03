def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i*i<=n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n=int(input())
result=0
for i in range(n, 1000001):
    if i==1:
        continue
    if str(i) == str(i)[::-1]:
        if is_prime(i):
            result=i
            break

if result == 0: 
    result = 1003001

print(result)
