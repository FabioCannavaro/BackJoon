n, k = map(int, input().split())

check=[0]*(n+1)
check[0]=1
check[1]=1

tmp=0
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if check[j]!=1:
            check[j]=1
            tmp+=1
            if tmp==k:
                print(j)