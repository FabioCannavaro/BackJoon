import sys
from collections import deque

def qu(lst, cmd):
    if cmd[0]=='1':
        lst.appendleft(int(cmd[1]))
    if cmd[0]=='2':
        lst.append(int(cmd[1]))
    if cmd[0]=='3':
        if len(lst)==0:
            print(-1)
        else:
            print(lst.popleft())
    if cmd[0]=='4':
        if len(lst)==0:
            print(-1)
        else:
            print(lst.pop())
    if cmd[0]=='5':
        print(len(lst))
    if cmd[0]=='6':
        if len(lst)==0:
            print(1)
        else:
            print(0)
    if cmd[0]=='7':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[0])
    if cmd[0]=='8':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[-1])

N=int(sys.stdin.readline())
lst=deque()
for i in range(N):
    cmd=sys.stdin.readline().split()
    qu(lst, cmd)