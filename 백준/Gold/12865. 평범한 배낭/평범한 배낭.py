N, K = map(int, input().split())
queue=[]
for i in range(N):
    W, V = map(int, input().split())
    queue.append([W, V])

dp=[0]*(K+1)

for w, v in queue:
    for j in range(K, w-1, -1):
        dp[j]=max(dp[j], dp[j-w]+v)

print(dp[-1])

