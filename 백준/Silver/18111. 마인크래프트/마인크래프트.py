import sys
input = sys.stdin.readline
n, m , b=map(int, input().split())
lst=[]
for i in range(n):
    ground=list(map(int, input().split()))
    lst.append(ground)

min_time = int(1e9)
max_height = 0

for height in range(257):
    blocks_added = 0
    blocks_removed = 0
    for i in range(n):
        g=lst[i]
        for j in range(m):
            if g[j]>=height:
                blocks_removed += g[j]-height
            else:
                blocks_added+=height-g[j]
    
    if blocks_added > blocks_removed+b:
        continue
    cost=blocks_removed*2+blocks_added
    if cost <= min_time:
        min_time = cost
        max_height = height

print(min_time, max_height)