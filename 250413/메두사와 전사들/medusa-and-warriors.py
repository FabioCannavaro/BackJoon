from collections import deque
import sys

n, m = map(int, input().split())
Sr, Sc, Er, Ec = map(int, input().split())
warriors = list(map(int, input().split()))
warriors_pos = []
warrior_pos = [(warriors[i], warriors[i+1]) for i in range(0, 2*m, 2)]

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs_medusa(start, end):
    visited = []
    for i in range(n):
        visited.append([-1]*n)
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = -2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx < n and 0<=ny <n and board[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = (x, y)
                queue.append((nx, ny))
                if (nx, ny) == end:
                    break
    if visited[end[0]][end[1]] == -1:
        return None
    # 경로 역추적
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = visited[cur[0]][cur[1]]
    path.append(start)
    path.reverse()
    return path

def get_sight_range(medusa_pos, warrior_pos_list, direction):
    r, c = medusa_pos
    vision = set()
    drc = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
    dx, dy = drc[direction]
    for dist in range(1, n):
        for spread in range(-dist, dist + 1):
            if direction == 0:
                nx, ny = r - dist, c + spread
            elif direction == 1:
                nx, ny = r + dist, c + spread
            elif direction == 2:
                nx, ny = r + spread, c - dist
            elif direction == 3:
                nx, ny = r + spread, c + dist
            if 0 <= nx < n and 0 <= ny < n:
                vision.add((nx, ny))
    return vision
def decide_best_direction(medusa_pos, warrior_pos_list):
    max_count = -1
    best_dir = 0
    best_seen = set()
    for d in range(4):
        visible = get_sight_range(medusa_pos, warrior_pos_list, d)
        count = sum((wx, wy) in visible for wx, wy in warrior_pos_list)
        if count > max_count:
            max_count = count
            best_dir = d
            best_seen = visible
    return best_dir, best_seen

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def move_warriors(warriors, medusa_pos, vision):
    total_move = 0
    new_positions = []
    for x, y in warriors:
        path = [(x, y)]
        for _ in range(2):
            best_dist = manhattan((x, y), medusa_pos)
            moved = False
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vision:
                    d = manhattan((nx, ny), medusa_pos)
                    if d < best_dist:
                        x, y = nx, ny
                        path.append((x, y))
                        total_move += 1
                        moved = True
                        break
            if not moved:
                break
        new_positions.append((x, y))
    return new_positions, total_move


medusa_path = bfs_medusa((Sr, Sc), (Er, Ec))
if medusa_path is None:
    print(-1)
    sys.exit()

turn = 0
medusa_idx = 0

while True:
    turn += 1
    # 1. 메두사 이동
    if medusa_idx + 1 < len(medusa_path):
        Sr, Sc = medusa_path[medusa_idx + 1]
        medusa_idx += 1

    # 2. 메두사 공격
    warrior_pos = [(x, y) for x, y in warrior_pos if (x, y) != (Sr, Sc)]

    # 3. 시야 계산
    best_dir, vision = decide_best_direction((Sr, Sc), warrior_pos)
    stoned = set()
    for x, y in warrior_pos:
        if (x, y) in vision:
            stoned.add((x, y))

    # 4. 전사 이동
    movable_warriors = [pos for pos in warrior_pos if pos not in stoned]
    warrior_pos, total_move = move_warriors(movable_warriors, (Sr, Sc), vision)

    # 5. 공격한 전사 처리
    kill = warrior_pos.count((Sr, Sc))
    warrior_pos = [(x, y) for x, y in warrior_pos if (x, y) != (Sr, Sc)]

    print(total_move, len(stoned), kill)

    if (Sr, Sc) == (Er, Ec):
        print(0)
        break