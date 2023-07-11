import sys
n=int(sys.stdin.readline())
if n == 0:
    print(0)
    exit()
lst=[]
for i in range(n):
    score=int(sys.stdin.readline())
    lst.append(score)
lst.sort()
cut_top=round(n*0.15+0.0000001)
cut_bottom=round(n*0.15+0.0000001)
for i in range(cut_top):
    lst.pop()
lst.reverse()
for i in range(cut_bottom):
    lst.pop()
lst.sort()
result=round((sum(lst)/len(lst))+0.0000001)
print(result)