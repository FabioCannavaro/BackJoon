n, m=map(int, input().split())
not_listen=set()
not_look=set()
for i in range(n):
    x=input()
    not_listen.add(x)
for i in range(m):
    y=input()
    not_look.add(y)
res=sorted(list(not_listen & not_look))
print(len(res))
for i in res:
    print(i)

