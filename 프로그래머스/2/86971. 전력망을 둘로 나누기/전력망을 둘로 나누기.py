from collections import deque

def bfs(adj_list, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1

    return count

def solution(n, wires):
    min_diff = float('inf')  
    adj_list = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    for v1, v2 in wires:
        adj_list[v1].remove(v2)
        adj_list[v2].remove(v1)

        visited = [False] * (n + 1)
        count1 = bfs(adj_list, v1, visited)
        count2 = bfs(adj_list, v2, visited)

        min_diff = min(min_diff, abs(count1 - count2))

        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    return min_diff