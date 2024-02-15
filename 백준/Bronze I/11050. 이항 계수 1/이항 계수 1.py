def factorial(num):
    res=1
    while num>0:
        res*=num
        num=num-1
    return res
N, K=map(int, input().split())

result=int(factorial(N)/(factorial(K)*factorial(N-K)))
print(result)