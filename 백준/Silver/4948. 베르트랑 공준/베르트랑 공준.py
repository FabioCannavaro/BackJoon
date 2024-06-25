check=[0]*(123456*2)
check[0]=1
check[1]=1

prime=[]
for i in range(2, (123456*2)):
    if check[i]==0:
        prime.append(i)
        for j in range(2*i, (123456*2), i):
            check[j]=1

while True:
    n=int(input())
    if n==0:
        break
    else:
        cnt=0
        for i in prime:
            if n<i<=2*n:
                cnt+=1
        print(cnt)