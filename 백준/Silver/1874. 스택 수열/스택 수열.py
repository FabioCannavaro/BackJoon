def check_stack(n, num):
    stack=[]
    result=[]
    current_num=1
    for i in num:
        while current_num<=i:
            stack.append(current_num)
            result.append('+')
            current_num+=1
        if stack[-1]==i:
            stack.pop()
            result.append('-')
        else:
            return 'NO'
        
    return '\n'.join(result)

if __name__ == '__main__':
    n=int(input())
    num=[]
    for i in range(n):
        lst=int(input())
        num.append(lst)
    answer=check_stack(n, num)
    if answer=='NO':
        print(answer)
    else:
        print(answer)