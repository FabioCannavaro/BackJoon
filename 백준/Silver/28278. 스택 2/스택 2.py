import sys

# 입력의 첫 줄을 읽어서 명령의 수 N을 정수로 변환합니다.
N = int(sys.stdin.readline().strip())
lst = []

for _ in range(N):
    # 명령을 읽습니다. split()은 문자열을 공백으로 구분하여 리스트로 만듭니다.
    # map 함수로 각각의 요소를 정수로 변환할 필요가 없이,
    # 입력 받은 명령을 직접 처리합니다.
    command = sys.stdin.readline().strip().split()
    
    if command[0] == '1': # 정수 X를 스택에 넣는 명령
        lst.append(int(command[1]))
    elif command[0] == '2': # 스택에서 정수를 빼는 명령
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif command[0] == '3': # 스택에 들어있는 정수의 개수를 출력
        print(len(lst))
    elif command[0] == '4': # 스택이 비어있는지 확인
        print(1 if not lst else 0)
    elif command[0] == '5': # 스택의 맨 위의 정수를 출력
        print(lst[-1] if lst else -1)
