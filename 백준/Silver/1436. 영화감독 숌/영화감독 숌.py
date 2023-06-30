def apocalyptic_number(n):
    cnt=0
    num=665
    while True:
        num+=1
        if "666" in str(num):
            cnt+=1
            if cnt==n:
                return num
n=int(input())
result=apocalyptic_number(n)
print(result)