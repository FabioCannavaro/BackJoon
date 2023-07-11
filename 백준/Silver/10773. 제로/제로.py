lst=[]
n=int(input())
for i in range(n):
    num=int(input())
    if num!=0:
        lst.append(num)
    elif num==0:
        lst.pop()
res=sum(lst)
print(res)