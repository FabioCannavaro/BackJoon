def GCD(m, n):
    gcd = []
    for i in range(1, min(m, n) + 1):
        if (m % i == 0 and n % i == 0):
            gcd.append(i)
    return print(max(gcd))

def LCM(m, n):
    lcm = max(m, n)
    while True:
        if lcm % m == 0 and lcm % n == 0:
            return print(lcm)
        lcm += 1

m, n = map(int, input().split())
GCD(m, n)
LCM(m, n)
