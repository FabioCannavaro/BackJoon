def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
n=int(input())
result=factorial(n)
cnt=0
while result > 0:
    digit = result % 10
    result //= 10
    cnt+=1
    if digit!=0:
        cnt-=1
        break
print(cnt)