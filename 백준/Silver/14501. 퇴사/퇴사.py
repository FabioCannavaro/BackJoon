n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int, input().split())))

dp=[0]*(n+5)
for i in range(n):
    for j in range(i+lst[i][0], n+1):
        if dp[j]<dp[i]+lst[i][1]:
            dp[j]=dp[i]+lst[i][1]
print(max(dp))
