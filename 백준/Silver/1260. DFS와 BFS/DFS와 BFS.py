from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 입력 받기
N, M, V = map(int, input().split())
graph = {}

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 정점 리스트 정렬
for vertex in graph:
    graph[vertex].sort()

# 방문 여부를 나타내는 리스트
visited = [False] * (N + 1)

# DFS 수행 및 출력
dfs(graph, V, visited)
print()

# BFS 수행 및 출력을 위해 visited 리스트 초기화
visited = [False] * (N + 1)

# BFS 수행 및 출력
bfs(graph, V, visited)
