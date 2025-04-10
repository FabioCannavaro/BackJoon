from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def move(board, x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x+=dx
        y+=dy
        cnt+=1
    return x, y, cnt
    
def bfs(board, red_x, red_y, blue_x, blue_y):
    queue = deque()
    queue.append((red_x, red_y, blue_x, blue_y, 0))
    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))
    while queue:
        rx, ry, bx, by, tmp = queue.popleft()
        
        if tmp >= 10:
            return -1
        for i in range(4):
            nrx, nry, rcnt = move(board, rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(board, bx, by, dx[i], dy[i])
            
            if board[nbx][nby] == 'O':
                continue
            elif board[nrx][nry] == 'O':
                return tmp + 1
            elif nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]
            if (nrx, nry, nbx, nby) not in visited:
                queue.append((nrx, nry, nbx, nby, tmp+1))
                visited.add((nrx, nry, nbx, nby))
    return -1
                
n, m = map(int, input().split())
lst = []
for i in range(n):
    row = list(input())
    lst.append(row)

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'R':
            red_x, red_y = i, j
        elif lst[i][j] == 'B':
            blue_x, blue_y = i, j
            

print(bfs(lst, red_x, red_y, blue_x, blue_y))