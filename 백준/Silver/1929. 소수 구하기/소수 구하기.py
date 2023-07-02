def prime_num(start, end):
    init_prime=[True]*(end+1)
    init_prime[0]=False
    init_prime[1]=False
    for i in range(2, int(end**0.5)+1):
        if init_prime[i]==True:
            for j in range(i*i, end+1, i):
                init_prime[j]=False

    primes = [i for i in range(start, end + 1) if init_prime[i]]
    return primes
if __name__=='__main__':
    m, n=map(int, input().split())
    res=prime_num(m,n)
    for i in res:
        print(i)