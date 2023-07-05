n=int(input())
members=[]
for i in range(n):
    age, name=input().split()
    age=int(age)
    members.append((age, name))
sort_members=sorted(members, key=lambda x: x[0])
for i in sort_members:
    print(i[0], i[1])