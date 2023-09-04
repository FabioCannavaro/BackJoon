prob=input().split('-')
num=[]
for i in prob:
    x=i.split('+')
    num.append(x)
    
result=[]
for i in num:
    total = 0
    for j in i:
        total += int(j)
    result.append(total)
res=result[0]
for i in range(1, len(result)):
    res-=result[i]
print(res)