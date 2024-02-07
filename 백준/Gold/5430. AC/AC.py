from collections import deque
import sys

T=int(input())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    lst = sys.stdin.readline().rstrip()[1:-1].split(',')
    
    dq = deque(lst) if n > 0 else deque()


    reverse = False
    error = False
    for i in p:
        if i =='R':
            reverse = not reverse
        elif i == 'D':
            if dq:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print("error")
                error = True
                break
    if not error:
        if reverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
    
