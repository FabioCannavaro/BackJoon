def check_color(paper, x, y, size):
    color = paper[x][y] 
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color: 
                return False
    return True

def divide_and_conquer(paper, x, y, size):
    if check_color(paper, x, y, size):
        if paper[x][y] == 0:
            white[0] += 1
        else:
            blue[0] += 1
    else:
        new_size = size // 2
        divide_and_conquer(paper, x, y, new_size)
        divide_and_conquer(paper, x, y + new_size, new_size)
        divide_and_conquer(paper, x + new_size, y, new_size)
        divide_and_conquer(paper, x + new_size, y + new_size, new_size)

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]

white = [0]
blue = [0]

divide_and_conquer(paper, 0, 0, n)

print(white[0])
print(blue[0])
