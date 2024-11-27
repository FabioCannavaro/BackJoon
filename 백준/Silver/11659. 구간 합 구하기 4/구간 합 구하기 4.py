import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num=list(map(int, input().split()))

prefixSum=[0]*(N+1)
for i in range(1, N+1):
    prefixSum[i]=num[i-1]+prefixSum[i-1]

for i in range(M):
    start, end = map(int, input().split())
    result = prefixSum[end]-prefixSum[start-1]
    print(result)