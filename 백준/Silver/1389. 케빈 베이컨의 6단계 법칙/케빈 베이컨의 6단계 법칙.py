from collections import deque

def bfs(graph, start):
    n=len(graph)
    visited=(n+1)*[False]
    kevin_bacon_sum=[0]*(n+1)
    queue=deque([(start, 0)])
    visited[start]=True
    

    while queue:
        
        person, kevin_bacon = queue.popleft()
        kevin_bacon_sum[person-1]=kevin_bacon
        for friend in graph[person]:
            if not visited[friend]:
                visited[friend] = True
                queue.append((friend, kevin_bacon+1))

    return kevin_bacon_sum
n, m=map(int, input().split())
graph = {}

for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_kevin_bacon = float('inf')
min_person = 0

for person in range(1, n + 1):
    kevin_bacon_sum = bfs(graph, person)
    total_kevin_bacon = sum(kevin_bacon_sum)
    
    if total_kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = total_kevin_bacon
        min_person = person

print(min_person)