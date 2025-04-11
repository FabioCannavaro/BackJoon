def get_shapes():
    return [
        # ㅡ
        [(0,0), (0,1), (0,2), (0,3)],
        # ㅣ
        [(0,0), (1,0), (2,0), (3,0)],
        # ㅁ
        [(0,0), (0,1), (1,0), (1,1)],
        # L과 J (회전 포함)
        [(0,0), (1,0), (2,0), (2,1)],
        [(0,0), (0,1), (0,2), (1,0)],
        [(0,0), (0,1), (1,1), (2,1)],
        [(1,0), (1,1), (1,2), (0,2)],
        [(0,0), (1,0), (2,0), (0,1)],
        [(0,0), (0,1), (1,1), (2,1)],
        [(0,0), (0,1), (0,2), (1,2)],
        [(0,0), (0,1), (1,0), (1,1)],
        # Z와 S
        [(0,0), (0,1), (1,1), (1,2)],
        [(1,0), (2,0), (0,1), (1,1)],
        [(0,0), (1,0), (1,-1), (2,-1)],
        [(0,0), (0,1), (-1,1), (-1,2)],
        # T (회전 포함)
        [(0,0), (0,1), (0,2), (1,1)],
        [(0,1), (1,0), (1,1), (2,1)],
        [(1,0), (1,1), (1,2), (0,1)],
        [(0,0), (1,0), (2,0), (1,1)],
    ]

def max_tetromino_sum(board):
    n, m = len(board), len(board[0])
    shapes = get_shapes()
    max_sum = 0

    for x in range(n):
        for y in range(m):
            for shape in shapes:
                total = 0
                for dx, dy in shape:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    total += board[nx][ny]
                max_sum = max(max_sum, total)


    return max_sum

def main():
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    print(max_tetromino_sum(board))

if __name__ == "__main__":
    main()
