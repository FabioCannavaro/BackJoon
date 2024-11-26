dp=[0]*12
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4, 12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

T=int(input())
result=[]
for i in range(T):
    n=int(input())
    result.append(dp[n])
for i in result:
    print(i)