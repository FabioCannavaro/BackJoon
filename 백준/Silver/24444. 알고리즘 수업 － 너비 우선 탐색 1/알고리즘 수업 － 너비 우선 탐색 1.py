from collections import deque
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(graph, start, visited):
    global cnt
    queue=deque([start])
    visited[start]=cnt

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                queue.append(i)
                cnt+=1
                visited[i]=cnt


N, M, R = map(int, input().split())
graph=[]
for i in range(N+1):
    graph.append([])

visited=[0]*(N+1)
cnt=1

for i in range(M):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()

bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])
