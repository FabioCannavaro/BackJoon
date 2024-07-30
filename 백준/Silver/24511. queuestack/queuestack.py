N=int(input())
types=list(map(int, input().split()))
start=list(map(int, input().split()))
M=int(input())
new=list(map(int, input().split()))

result=[]
for i in range(N):
    if types[-(i+1)]==0:
        result.append(start[-(i+1)])

for i in range(M):
    result.append(new[i])

for i in range(M):
    print(result[i], end=' ')