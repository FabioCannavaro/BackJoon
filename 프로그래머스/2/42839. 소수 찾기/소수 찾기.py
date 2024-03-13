import math
import itertools
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        for perm in itertools.permutations(numbers, i):
            num = int(''.join(perm))
            all_numbers.add(num)
    for num in all_numbers:
        if num==1 or num==0:
            continue
        else:
            if isPrime(num):
                answer += 1

    return answer