import copy
def move_left(board):
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j]=0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor]*=2
                    cursor+=1
                else:
                    cursor+=1
                    board[i][cursor] = tmp
    return board

def move_right(board):
    for i in range(n):
        cursor = n-1
        for j in range(n-1, -1, -1):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j]=0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor]*=2
                    cursor-=1
                else:
                    cursor-=1
                    board[i][cursor] = tmp
    return board

def move_up(board):
    for j in range(n):
        cursor = 0
        for i in range(n):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j]=0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j]*=2
                    cursor+=1
                else:
                    cursor+=1
                    board[cursor][j] = tmp
    return board


def move_down(board):
    for j in range(n):
        cursor = n-1
        for i in range(n-1, -1, -1):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j]=0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j]*=2
                    cursor-=1
                else:
                    cursor-=1
                    board[cursor][j] = tmp
    return board

def dfs(depth, board):
    global result
    if depth == 5:
        for i in range(n):
            for j in range(n):
                if board[i][j] > result:
                    result = board[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(board)
        if i == 0:
            dfs(depth +1, move_left(copy_arr))
        elif i == 1:
            dfs(depth + 1, move_right(copy_arr))
        elif i == 2:
            dfs(depth + 1, move_up(copy_arr))
        else:
            dfs(depth + 1, move_down(copy_arr))

n = int(input())
board = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

result = 0
dfs(0, board)
print(result)