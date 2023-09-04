from collections import deque

def bfs(start, end):
    visited=[False]*100001
    queue=deque([(start, 0)])
    visited[start]=True
    
    while queue:
        position, time=queue.popleft()
        if position==end:
            return time
        walk_teleport=[position-1, position+1, position*2]

        for i in walk_teleport:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                queue.append((i, time + 1))

n, k=map(int, input().split())
result=bfs(n,k)
print(result)
