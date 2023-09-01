n=int(input())
dp={1:0}

def make_one(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(make_one(n//3)+1, make_one(n//2)+1)
    elif n%3==0:
        dp[n]=min(make_one(n//3)+1, make_one(n-1)+1)
    elif n%2==0:
        dp[n]=min(make_one(n//2)+1, make_one(n-1)+1)
    else:
        dp[n]=make_one(n-1)+1
    return dp[n]
print(make_one(n))