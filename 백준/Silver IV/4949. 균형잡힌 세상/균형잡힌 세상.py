def balance(st):
    lst=[]
    for i in st:
        if i =='(' or i == '[':
            lst.append(i)
        elif i ==')':
            if not lst or lst[-1] != '(':
                return False
            lst.pop()
        elif i ==']':
            if not lst or lst[-1] != '[':
                return False
            lst.pop()
    return not lst
    
while True:
    st=input()
    if st == '.':
        break
    elif balance(st):
        print("yes")
    else:
        print("no")