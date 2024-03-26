from collections import deque

def solution(tickets):
    answer = []
    queue=deque()
    queue.append(("ICN", ["ICN"], []))
    while queue:
        airport, path, used = queue.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                queue.append((ticket[1], path+[ticket[1]], used+[idx]))

    answer.sort(key=len)

    answer = sorted(answer, key=lambda x: x[1:])  

    return answer[0]