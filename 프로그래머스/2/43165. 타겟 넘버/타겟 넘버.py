from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        a, b=queue.popleft()
        b+=1
        if b<n:
            queue.append([a+numbers[b], b])
            queue.append([a-numbers[b], b])
        else:
            if a==target:
                answer+=1
    return answer