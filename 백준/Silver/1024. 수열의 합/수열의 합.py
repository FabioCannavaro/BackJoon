n, l=map(int, input().split())
for i in range(l, 101):
    an=n-(i*(i+1)//2)
    if an%i==0:
        x=an//i
        if x+1>=0:
            res=(i for i in range(x+1, x+i+1))
            print(*res)
            break
else:
    print(-1)