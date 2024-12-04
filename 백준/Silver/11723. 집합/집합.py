import sys
input = sys.stdin.readline
m = int(input().strip())
S = set()
for i in range(m):
    commands = list(input().split())
    x = 0
    if len(commands) >= 2:
        x = commands[1]
    command = commands[0]

    if command == 'add':
        S.add(x)
    elif command == 'remove':
        S.discard(x)
    elif command == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif command == 'all':
        S = set(str(i) for i in range(1, 21))
    else:
        S = set()