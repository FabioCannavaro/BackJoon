from collections import deque

def generate_primes():
    is_prime = [True] * 10000
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(10000**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, 10000, i):
                is_prime[j] = False
                ###에뭐시기 체 써서 소수판별

    return is_prime

def bfs(start, end, is_prime):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current, cnt = queue.popleft()
        
        for i in range(4): ##한자릿수씩
            for j in range(10): ##0~9까지 돌린다
                next_num = list(str(current)) #숫자를 문자열로 변환 후 리스트 형식으로 바꿔줌 ex) 1234=['1', '2', '3', '4']
                next_num[i] = str(j) #0번째부터 한자릿수씩 0~9까지 숫자바꿔서 변환
                next_num = int(''.join(next_num)) #바꾸고 다시 숫자로 변환
                
                if next_num >= 1000 and is_prime[next_num] and next_num not in visited: ##위에서 바꾼게 4자릿수이고, 소수이면서, 아직 방문하지 않았을 경우
                    if next_num == end: ##최종결과면
                        return cnt + 1 #cnt +1 하고 리턴
                    visited.add(next_num)  
                    queue.append((next_num, cnt + 1)) ##다시 탐색 ㄱ고고
    
    return "Impossible"


is_prime = generate_primes()
    
T = int(input())
for i in range(T):
    start, end = map(int, input().split())
    print(bfs(start, end, is_prime))