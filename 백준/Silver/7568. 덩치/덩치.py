lst=[]
rank=[]
n=int(input())
for i in range(n):
    x, y=map(int, input().split())
    lst.append((x,y))
for i in lst:
    cnt=1
    for j in lst:
        if i[0]<j[0] and i[1]<j[1]:
            cnt+=1
    rank.append(cnt)
print(*rank)