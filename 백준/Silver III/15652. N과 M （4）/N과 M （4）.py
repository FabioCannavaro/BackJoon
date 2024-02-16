def dfs(start):
    if len(res)==M:
        print(' '.join(map(str,res)))
        return

    for i in range(start, N+1):
        visited[i]=True
        res.append(i)
        dfs(i)
        res.pop()
        visited[i]=False

N, M = map(int, input().split())
res=[]
visited=[False] * (N+1)
start=1
dfs(start)