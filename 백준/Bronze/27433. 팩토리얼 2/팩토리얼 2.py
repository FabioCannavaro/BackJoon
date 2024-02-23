def factorial(n):
    res=1
    while n>0:
        res*=n
        n=n-1
    return res
N=int(input())
print(factorial(N))