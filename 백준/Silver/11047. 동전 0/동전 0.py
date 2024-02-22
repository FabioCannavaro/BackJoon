N, K = map(int, input().split())
coin=[]
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
res=0
for i in coin:
    if K>=i:
        res+=K//i
        K%=i
        if K<=0:
            break
print(res)