from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue=deque(truck_weights)
    time=0
    bridge=deque([0] * bridge_length)
    currentweight=0
    while queue:
        time+=1
        currentweight-=bridge.popleft()
        if currentweight+queue[0]<=weight:
            currentweight+=queue[0]
            bridge.append(queue.popleft())
        else:
            bridge.append(0)
    time+=bridge_length
    answer=time
    return answer