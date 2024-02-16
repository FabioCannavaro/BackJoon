def dfs(start):
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    for i in range(start, N+1):
        if visited[i]==True:
            continue
        visited[i]=True
        res.append(i)   
        dfs(i+1)
        res.pop()
        visited[i]=False

N, M=map(int, input().split())
visited=[False] * (N+1)
res=[]
start=1
dfs(start)