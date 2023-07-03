def prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n=int(input())
num=list(map(int, input().split()))
cnt=0
for i in range(n):
    if prime(num[i]):
        cnt+=1
print(cnt)