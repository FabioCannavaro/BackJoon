# 방향: 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 인덱스
bottom = 0
top = 1
front = 2
back = 3
left = 4
right = 5

n, m, x, y, k = map(int, input().split())

lst = []
for i in range(n):
    row = list(map(int, input().split()))
    lst.append(row)

num = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

def roll_dice(dir):
    global dice
    t, b, f, ba, l, r = dice[top], dice[bottom], dice[front], dice[back], dice[left], dice[right]

    if dir == 1:  # 동
        dice[top], dice[bottom], dice[left], dice[right] = l, r, b, t
    elif dir == 2:  # 서
        dice[top], dice[bottom], dice[left], dice[right] = r, l, t, b
    elif dir == 3:  # 북
        dice[top], dice[bottom], dice[front], dice[back] = f, ba, b, t
    elif dir == 4:  # 남
        dice[top], dice[bottom], dice[front], dice[back] = ba, f, t, b


cur_x, cur_y = x, y

for i in num:
    nx = cur_x + dx[i-1]
    ny = cur_y + dy[i-1]

    if not (0<= nx < n and 0 <= ny < m):
        continue


    roll_dice(i)
    
    if lst[nx][ny] == 0:
        lst[nx][ny] = dice[bottom]
    else:
        dice[bottom] = lst[nx][ny]
        lst[nx][ny] = 0

    print(dice[top])

    cur_x, cur_y = nx, ny
