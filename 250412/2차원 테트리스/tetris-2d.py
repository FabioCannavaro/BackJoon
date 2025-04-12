from collections import deque

def yellow_put(t, x, y):
    if t == 1:
        return [[1, y]]
    elif t == 2:
        return [[1, y], [1, y + 1]]
    elif t == 3:
        return [[0, y], [1, y]]

def red_put(t, x, y):
    if t == 1:
        return [[1, x]]
    elif t == 2:
        return [[0, x], [1, x]]
    elif t == 3:
        return [[1, x], [1, x + 1]]

def down(board, block):
    moved = [b[:] for b in block]
    while True:
        can_move = True
        for x, y in moved:
            if x + 1 >= 6 or board[x + 1][y] == 1:
                can_move = False
                break
        if not can_move:
            break
        for b in moved:
            b[0] += 1
    for x, y in moved:
        board[x][y] = 1

def check(board):
    score = 0
    i = 2
    while i < 6:
        if sum(board[i]) == 4:
            del board[i]
            board.appendleft([0, 0, 0, 0])
            score += 1
        else:
            i += 1

    light_cnt = 0
    for i in [0, 1]:
        if any(board[i]):
            light_cnt += 1
    for _ in range(light_cnt):
        board.pop()
        board.appendleft([0, 0, 0, 0])
    return score

def result(yellows, reds):
    cnt = 0
    for i in range(2, 6):
        cnt += sum(yellows[i])
        cnt += sum(reds[i])
    return cnt

k = int(input())
yellows = deque([[0]*4 for _ in range(6)])
reds = deque([[0]*4 for _ in range(6)])
answer = 0

for _ in range(k):
    t, x, y = map(int, input().split())
    yellow = yellow_put(t, x, y)
    red = red_put(t, x, y)

    down(yellows, yellow)
    down(reds, red)

    answer += check(yellows)
    answer += check(reds)

print(answer)
print(result(yellows, reds))
