def check(board):
    start_white=0
    start_black=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and board[i][j]=='B':
                start_white+=1
            elif (i+j)%2==1 and board[i][j]=='W':
                start_white+=1
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and board[i][j]=='W':
                start_black+=1
            elif (i+j)%2==1 and board[i][j]=='B':
                start_black+=1
    return min(start_white, start_black)

def min_repaint(m, n, board):
    min_count = float('inf')
    for i in range(m - 7):
        for j in range(n - 7):
            sub_board = [row[j:j+8] for row in board[i:i+8]]
            count = check(sub_board)
            min_count = min(min_count, count)

    return min_count

m, n = map(int, input().split())
board=[]
for i in range(m):
    row=input()
    board.append(row)
result=min_repaint(m,n,board)
print(result)