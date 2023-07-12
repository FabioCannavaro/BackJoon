def fibonacci(n):
    if n==0:
        return [1,0]
    if n==1:
        return [0,1]
    
    fibo=[0]*(n+1)
    cnt=[[0,0]for i in range(n+1)]
    fibo[0]=0
    fibo[1]=1
    cnt[0]=[1,0]
    cnt[1]=[0,1]
    
    for i in range(2, n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
        cnt[i][0]=cnt[i-1][0]+cnt[i-2][0]
        cnt[i][1]=cnt[i-1][1]+cnt[i-2][1]
    return cnt[n]

n=int(input())
for i in range(n):
    num=int(input())
    res=fibonacci(num)
    print(res[0], res[1])