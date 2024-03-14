from collections import deque
def solution(n, computers):
    answer = 0
    
    def bfs(start, visited, computers):
        visited[start]=True
        queue=deque()
        queue.append(start)
        while queue:
            v=queue.popleft()
            for i in range(n):
                if computers[v][i]==1 and not visited[i]:
                    visited[i]=True
                    queue.append(i)
    visited=[False] * (n)
    for i in range(n):
        if visited[i]==False:
            bfs(i, visited, computers)
            answer+=1
    return answer