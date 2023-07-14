def organic(m, n, k, cabbages):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    groups = 0
    visited = []
    for _ in range(n):
        visited.append([False] * m)

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            curr_x, curr_y = stack.pop()
            visited[curr_y][curr_x] = True
            for dx, dy in directions:
                next_x, next_y = curr_x + dx, curr_y + dy
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_y][next_x] and (next_x, next_y) in cabbages:
                    stack.append((next_x, next_y))

    for cabbage in cabbages:
        x, y = cabbage
        if not visited[y][x]:
            dfs(x, y)
            groups += 1

    return groups

def count_cabbage_worms(T, test):
    results = []
    for i in range(T):
        M, N, K, cabbages = test[i]
        groups = organic(M, N, K, cabbages)
        results.append(groups)
    return results

T = int(input())
test = []
for i in range(T):
    M, N, K = map(int, input().split())
    cabbages = []
    for _ in range(K):
        X, Y = map(int, input().split())
        cabbages.append((X, Y))
    test.append((M, N, K, cabbages))

results = count_cabbage_worms(T, test)
for result in results:
    print(result)
