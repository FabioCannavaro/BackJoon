from collections import deque

def card(lst):
    while True:
        if len(lst)>1:
            lst.popleft()
            a=lst.popleft()
            lst.append(a)
        else:
            print(lst[0])
            break

N=int(input())
lst=deque()
for i in range(1, N+1):
    lst.append(i)
card(lst)
