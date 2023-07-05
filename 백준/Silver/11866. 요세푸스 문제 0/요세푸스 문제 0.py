from collections import deque

n, k=map(int, input().split())
lst=deque(range(1, n+1))
res=[]
while lst:
    for i in range(k-1):
        lst.rotate(-1)
    res.append(lst.popleft())
    if len(lst)<1:
        break
print("<"+", ".join(map(str, res))+">")