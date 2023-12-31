def maximum(stair):
    a=len(stair)
    if a==0:
        return 0

    elif a==1:
        return print(stair[0])

    dp = a * [0]
    dp[0] = stair[0]
    dp[1] = max(stair[1], stair[0]+stair[1])

    for i in range(2, a):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    return print(dp[-1])

n=int(input())
stair=[]
for i in range(n):
    s=int(input())
    stair.append(s)
maximum(stair)

