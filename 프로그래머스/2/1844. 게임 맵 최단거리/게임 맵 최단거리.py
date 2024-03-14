from collections import deque
def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    def bfs(a,b, answer):
        queue=deque()
        queue.append((a,b))
        while queue:
            size=len(queue)
            answer+=1
            for i in range(size):
                a, b=queue.popleft()
                for j in range(4):
                    nx=a+dx[j]
                    ny=b+dy[j]
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                    if maps[nx][ny]==0:
                        continue
                    if maps[nx][ny]==1:
                        if nx==n-1 and ny==m-1:
                            return answer
                        maps[nx][ny]=0
                        queue.append((nx, ny))

        return -1
    return bfs(0,0,1)