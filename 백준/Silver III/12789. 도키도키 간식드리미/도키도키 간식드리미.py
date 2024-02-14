from collections import deque
N=int(input())
line=deque(map(int, input().split()))
stack=[]
cnt=1
while line:
    if line[0]==cnt:
        line.popleft()
        cnt+=1
    else:
        if stack and stack[-1]==cnt:
            stack.pop()
            cnt+=1
        else:
            stack.append(line.popleft())
while stack:
    if stack[-1]==cnt:
        stack.pop()
        cnt+=1
    else:
        break

if not stack and cnt-1 == N:
    print("Nice")
else:
    print("Sad")