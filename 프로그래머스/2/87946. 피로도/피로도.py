from itertools import permutations
def solution(k, dungeons):
    answer=[]
    lst = []
    for i in range(len(dungeons)):
        lst.append(i)
    trial = list(permutations(lst, len(lst)))
    for i in trial:
        cnt=0
        temp=k
        for j in i:
            if dungeons[j][0]<=temp:
                temp-=dungeons[j][1]
                cnt+=1
            else:
                break
        answer.append(cnt)

    return max(answer)