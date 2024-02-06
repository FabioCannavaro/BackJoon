from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    cnt=1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt         

num = int(input())
graph=[]
for i in range(num):
    graph.append(list(map(int, input())))


count = []
for i in range(num):
    for j in range(num):
        if graph[i][j] == 1:
            count.append(bfs(graph, i, j))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])



