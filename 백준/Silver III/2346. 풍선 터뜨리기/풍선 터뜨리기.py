import sys
from collections import deque

def balloon(num,N):
    lst=deque()
    res=[]
    for i in range(1, len(num)+1):
        lst.append((num[i-1],i))
    while lst:
        move, idx = lst.popleft()
        res.append(idx)
        if move>0:
            lst.rotate(-(move-1))
        else:
            lst.rotate(-move)
    return res
N=int(sys.stdin.readline())
num = deque(list(map(int, (sys.stdin.readline().strip().split()))))

result=balloon(num, N)
print(" ".join(map(str, result)))
