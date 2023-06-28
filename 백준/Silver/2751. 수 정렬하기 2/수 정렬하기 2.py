import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for i in range(n):
    num=int(input())
    lst.append(num)
lst.sort()
for j in lst:
    print(j)