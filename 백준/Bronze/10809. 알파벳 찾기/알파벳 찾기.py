S = input()
st ='abcdefghijklmnopqrstuvwxyz'

for i in st:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')