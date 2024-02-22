import sys
sys.setrecursionlimit(10 ** 4)

def is_valid(x, y, num):
    # 같은 행에 num이 있는지 확인
    for i in range(9):
        if board[x][i] == num:
            return False
    # 같은 열에 num이 있는지 확인
    for i in range(9):
        if board[i][y] == num:
            return False
    # 같은 3x3 박스에 num이 있는지 확인
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_x + i][start_y + j] == num:
                return False
    return True

def solve_sudoku():
    # 모든 칸을 확인
    for x in range(9):
        for y in range(9):
            # 빈 칸을 찾으면
            if board[x][y] == 0:
                # 가능한 모든 숫자(1~9)를 시도
                for num in range(1, 10):
                    if is_valid(x, y, num):
                        board[x][y] = num
                        if solve_sudoku():
                            return True
                        board[x][y] = 0  # 백트래킹
                return False
    return True


# 스도쿠 판 입력 받기
board=[]
for i in range(9):
    row=list(map(int, sys.stdin.readline().split()))
    board.append(row)

solve_sudoku()

# 완성된 스도쿠 판 출력
for row in board:
    print(' '.join(map(str, row)))
