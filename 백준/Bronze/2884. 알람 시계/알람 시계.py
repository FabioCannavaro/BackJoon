def ch_time(h, m):
    if m>=45:
        print(h, m-45)
    else:
        if h==0:
            h=23
        else:
            h=h-1
        m=m+15
        print(h, m)
h, m=map(int, input().split())
ch_time(h, m)