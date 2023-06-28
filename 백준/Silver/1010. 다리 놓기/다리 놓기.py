def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
num=int(input())
for i in range(num):
    n, m=map(int, input().split())
    bri=factorial(m)/(factorial(n)*factorial(m-n))
    print(int(bri))