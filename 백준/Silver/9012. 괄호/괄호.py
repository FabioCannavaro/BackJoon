def VPS(result):
    lst=[]
    for i in result:
        if i=="(":
            lst.append(i)
        elif i==")":
            if lst and lst[-1]=="(":
                lst.pop()
            else:
                return False
    return not lst
n=int(input())
for i in range(n):
    result=input()
    if VPS(result):
        print("YES")
    else:
        print("NO")
            