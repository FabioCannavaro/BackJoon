n=int(input())
s=input()
lst=[]
for i in range(n):
    lst.append((ord(s[i])-96)*(31**i))
res=sum(lst)
print(res)