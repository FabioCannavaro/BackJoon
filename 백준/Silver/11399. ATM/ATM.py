N=int(input())
time=list(map(int, input().split()))
time.sort()
current_time=0
total_time=0
for i in time:
    current_time+=i
    total_time+=current_time

print(total_time)
