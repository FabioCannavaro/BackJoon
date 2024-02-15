from collections import deque

def Josephus(table, k):
    lst=[]
    while True:
        if len(table)>0:
            table.rotate(-(k-1))
            lst.append(table.popleft())
        else:
            print("<"+", ".join(map(str, lst))+">")
            break
        
N, K=map(int, input().split())
table=deque()
for i in range(1, N+1):
    table.append(i)
Josephus(table, K)