def factorial(N):
    res=1
    while N>0:
        res*=N
        N=N-1
    return res
N=int(input())
print(factorial(N))