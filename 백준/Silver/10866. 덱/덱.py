from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    action = sys.stdin.readline().split()

    if action[0] == 'push_front':
        queue.append(int(action[1]))
        
    elif action[0] == 'push_back':
        queue.appendleft(int(action[1]))
        
    elif action[0] == 'pop_front':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif action[0] == 'pop_back':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif action[0] == 'size':
        print(len(queue))
        
    elif action[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
            
    elif action[0] == 'front':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif action[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)

