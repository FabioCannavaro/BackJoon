from itertools import permutations

N = int(input())  
A = list(map(int, input().split()))  
add, sub, mul, div = map(int, input().split())

operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div

##값들 초기화
max_result = -float('inf')
min_result = float('inf')

for ops in set(permutations(operators, N - 1)):
    result = A[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += A[i + 1]
        elif op == '-':
            result -= A[i + 1]
        elif op == '*':
            result *= A[i + 1]
        elif op == '/':
            if result < 0:
                result = -(-result // A[i + 1])
            else:
                result //= A[i + 1]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
