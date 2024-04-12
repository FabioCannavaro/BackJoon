from collections import deque

n=int(input())
k=int(input())

board=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    board.append(row)

for i in range(k):
    a, b=map(int, input().split())
    board[a-1][b-1]=1

l=int(input())
change=[]
for i in range(l):
    c, d=map(str, input().split())
    change.append((int(c), d))


dir=1
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

queue=deque()
queue.append((0,0))
cnt=0
l_cnt=0

def self_body(nx, ny, queue):
    for i in queue:
         if nx == i[0] and ny == i[1]:
             return True
    return False

while queue:

    x, y=queue[0][0], queue[0][1]

    nx=x+dx[dir]
    ny=y+dy[dir]
    cnt+=1

    if 0 <= nx < n and 0 <= ny < n:

        if self_body(nx, ny, queue):
            break

        if board[nx][ny]==0:
            queue.pop()
        else:
            board[nx][ny]=0
        queue.appendleft((nx, ny))

        if l_cnt<l:
            if change[l_cnt][0]==cnt:
                if change[l_cnt][1]=='L':
                    dir=(dir+3)%4
                else:
                    dir=(dir+1)%4
                l_cnt+=1
    else:
        break
print(cnt)


