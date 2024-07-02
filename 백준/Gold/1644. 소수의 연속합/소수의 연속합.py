n=int(input())

check=[0]*(n+1)
check[0]=1
check[1]=1

prime=[]
for i in range(2, n+1):
    if check[i]==0:
        prime.append(i)
        for j in range(2*i, n+1, i):
            check[j]=1


answer = 0
start = 0
end = 0
while end <= len(prime):
    tmp = sum(prime[start:end])
    if tmp == n:
        answer += 1
        end += 1
    elif tmp < n:
        end += 1
    else:
        start += 1

print(answer)