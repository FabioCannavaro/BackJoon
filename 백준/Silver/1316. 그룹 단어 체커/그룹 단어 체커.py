num=int(input())
cnt=0
for i in range(num):
    s=input()
    checked=set()
    prev_char=None
    group_word=True
    for char in s:
        if char in checked:
            if char != prev_char:
                group_word=False
                break
        else:
            checked.add(char)
            prev_char=char
    if group_word:
        cnt+=1
print(cnt)