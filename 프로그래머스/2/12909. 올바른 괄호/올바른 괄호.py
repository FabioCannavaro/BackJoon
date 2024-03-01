from collections import deque
def solution(s):
    answer = True
    queue=deque()
    for i in s:
        if i=='(':
            queue.append(i)
        elif i==')':
            if not queue or queue[-1]!='(':
                return False
            queue.pop()
    return not queue

    return True