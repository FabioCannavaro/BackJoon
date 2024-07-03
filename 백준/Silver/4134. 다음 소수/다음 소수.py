import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    if n <= 2:
        return 2
    prime = n
    if prime % 2 == 0:
        prime += 1
    while not is_prime(prime):
        prime += 2
    return prime

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(next_prime(n))

if __name__ == "__main__":
    main()
