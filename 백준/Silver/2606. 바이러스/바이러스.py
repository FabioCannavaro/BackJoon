from collections import deque

def bfs(n, net):
    graph = [[] for i in range(n+1)]
    visited= [False] * (n+1)
    for a, b in net:
        graph[a].append(b)
        graph[b].append(a)
        
    queue=deque([1])
    visited[1]=True

    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return count - 1

n=int(input())
m=int(input())
net=[]
for i in range(m):
    a, b = map(int, input().split())
    net.append((a, b))
print(bfs(n, net))