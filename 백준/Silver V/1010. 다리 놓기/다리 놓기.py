def factorial(num):
    res=1
    while num>0:
        res*=num
        num=num-1
    return res
T=int(input())
for i in range(T):
    N, M = map(int, input().split())
    result=int(factorial(M)/(factorial(N)*factorial(M-N)))
    print(result)