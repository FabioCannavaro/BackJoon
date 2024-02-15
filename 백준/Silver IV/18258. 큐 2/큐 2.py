from collections import deque
import sys

def qu(cmd, lst):
    if cmd[0]=='push':
        lst.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[0])
            lst.popleft()
    elif cmd[0]=='size':
        print(len(lst))
    elif cmd[0]=='empty':
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[0])
    elif cmd[0]=='back':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[-1])
N=int(sys.stdin.readline())
lst=deque()
for i in range(N):
    cmd=sys.stdin.readline().split()
    qu(cmd, lst)

