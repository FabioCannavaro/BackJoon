from collections import deque
N, K = map(int, input().split())
queue=[]
result=deque()
for i in range(N):
    W, V = map(int, input().split())
    queue.append([W, V])
    queue.sort(key=lambda x: x[0])
queue=deque(queue)

dp=[0]*(K+1)

for w, v in queue:
    for j in range(K, w-1, -1):
        dp[j]=max(dp[j], dp[j-w]+v)

print(dp[-1])

