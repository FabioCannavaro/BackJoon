from collections import deque
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    now_night = list(map(int, input().split()))
    next_night = list(map(int, input().split()))   

    visited=[]
    for i in range(n):
        row=[False]*n
        visited.append(row)
    matrix=[]
    for i in range(n):
        row=[0]*n
        matrix.append(row)

    queue=deque()

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs():
        queue.append(now_night)
        visited[now_night[0]][now_night[1]]

        while queue:
            x, y = queue.popleft()

            if x == next_night[0] and y == next_night[1] :
                return 0

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx <0 or nx>=n or ny<0 or ny>=n:
                    continue

                if nx == next_night[0] and ny == next_night[1]:
                    visited[nx][ny] = True
                    return matrix[x][y]+1

                if visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[x][y] + 1   
    print(bfs())