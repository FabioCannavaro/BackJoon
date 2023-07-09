def balanced_world(s):
    lst=[]
    open_bracket=['(' ,'[']
    close_bracket=[')', ']']
    for char in s:
        if char in open_bracket:
            lst.append(char)
        elif char in close_bracket:
            if not lst or open_bracket.index(lst.pop())!= close_bracket.index(char):
                return False
    return len(lst)==0
while True:
    s=input()
    if s=='.':
        break
    res="yes" if balanced_world(s) else "no"
    print(res)