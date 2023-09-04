import sys
input = sys.stdin.readline

n, m=map(int, input().split())
pokemon={}
pokemon_num={}
for i in range(1, n+1):
    x=input().strip()
    pokemon[x]=i
    pokemon_num[i]=x
for i in range(m):
    y=input().strip()
    if y.isdigit():
        num=int(y)
        print(pokemon_num[num])
    else:
        print(pokemon[y])