w=input()
w=w.upper()
lst=list(set(w))
cnt=[]
for i in lst:
    c=w.count(i)
    cnt.append(c)
if cnt.count(max(cnt))>1:
    print("?")
else:
    print(lst[cnt.index(max(cnt))])