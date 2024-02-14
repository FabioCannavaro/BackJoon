def Parenthesis(st):
    lst=[]
    for i in st:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst and lst[-1]=='(':
                lst.pop()
            else:
                return False
    return not lst
T=int(input())
for i in range(T):
    st=input()
    if Parenthesis(st):
        print("YES")
    else:
        print("NO")