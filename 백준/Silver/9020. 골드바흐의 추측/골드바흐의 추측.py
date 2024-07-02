def prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

T=int(input())
for i in range(T):
    num=int(input())
    a = num//2
    b = num//2
    while a>0:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1