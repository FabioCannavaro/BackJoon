n=int(input())
lst=[]
cnt=1

for i in range(n):
    s, e = map(int, input().split())
    lst.append((s,e))

lst.sort(key=lambda x: (x[1], x[0]))
end=lst[0][1]
for i in range(1, n):
    if lst[i][0]>=end:
        cnt+=1
        end=lst[i][1]
print(cnt)