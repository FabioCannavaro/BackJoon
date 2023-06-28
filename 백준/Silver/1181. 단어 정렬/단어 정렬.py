num=int(input())
str_list=set()
for i in range(num):
    s=input()
    str_list.add(s)
word=list(str_list)
word.sort(key=lambda x:(len(x), x))
for i in word:
    print(i)