n=int(input())
subject=list(map(int, input().split()))
max_sub=max(subject)
tot=sum(subject)
for i in range(len(subject)):
    subject[i]=subject[i]/max_sub*100
ch_avg=sum(subject)/len(subject)
print(ch_avg)