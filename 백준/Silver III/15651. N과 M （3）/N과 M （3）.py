def dfs():
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):

        visited[i]=True
        res.append(i)   
        dfs()
        res.pop()
        visited[i]=False

N, M=map(int, input().split())
visited=[False] * (N+1)
res=[]
dfs()