import sys
sys.setrecursionlimit(10 ** 4)

N=int(sys.stdin.readline())
S=[]

low=float('inf')
for i in range(N):
    n=list(map(int, sys.stdin.readline().split()))
    S.append(n)

def divide_team(start, team):
    global low
    if len(team) == N/2:
        s_team=0
        l_team=0
        for i in range(N):
            for j in range(N):
                if i in team and j in team:
                    s_team+=S[i][j]
                elif i not in team and j not in team:
                    l_team+=S[i][j]
        low=min(low, abs(s_team-l_team))
        return
    for i in range(start, N):
        divide_team(i+1, team+[i])


divide_team(0, [])

print(low)