check=[0]*(1000001)
check[0]=1
check[1]=1

for i in range(2, int(len(check) ** 0.5)+1):
    if check[i]==0:
        for j in range(2*i, 1000001, i):
            check[j]=1

while True:
    num=int(input())
    if num==0:
        break
    for i in range(3, num-2, 2):
        if (check[i]==0) and (check[num-i]==0):
            print(f"{num} = {i} + {num-i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')