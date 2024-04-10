from collections import deque

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]
def bfs(rx, ry, bx, by):
    queue=deque()
    queue.append((rx, ry, bx, by))
    visited=[]
    visited.append((rx, ry, bx, by))
    cnt=0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by=queue.popleft()
            if cnt>10:
                return -1
            if board[rx][ry]=='O':
                return cnt
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx+=dx[i]
                    nry+=dy[i]
                    if board[nrx][nry]=='#':
                        nrx-=dx[i]
                        nry-=dy[i]
                        break
                    if board[nrx][nry]=='O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx+=dx[i]
                    nby+=dy[i]
                    if board[nbx][nby]=='#':
                        nbx-=dx[i]
                        nby-=dy[i]   
                        break
                    if board[nbx][nby]=='O':
                        break
                if board[nbx][nby]=='O':
                    continue
                if nrx==nbx and nry==nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt+=1                  
    return -1
    
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j]=='R':
            rx, ry=i, j
        elif board[i][j]=='B':
            bx, by=i,j

result=bfs(rx, ry, bx, by)
print(result)