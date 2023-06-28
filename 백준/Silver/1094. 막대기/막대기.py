init=64
x=int(input())
cnt=0
while(1):
    if (x<init):
        init=init//2
    else:
        x=x-init
        cnt+=1
        if x==0:
            break
print(cnt)