from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited=[0] * (N+1)
lst=[]
for i in range(N+1):
    lst.append([])

cnt=1

def DFS(graph, v, visited):
    global cnt
    visited[v]=cnt
    for i in graph[v]:
        if visited[i]==0:
            cnt+=1
            DFS(graph, i, visited)


for i in range(M):
    a, b=map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in range(N+1):
    lst[i].sort()

DFS(lst, R, visited)

for i in range(1, N+1):
    print(visited[i])





