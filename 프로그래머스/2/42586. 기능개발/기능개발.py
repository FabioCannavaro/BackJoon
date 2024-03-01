def solution(progresses, speeds):
    answer = []
    lst=[]
    for i in range(len(speeds)):
        cnt=0
        while True:
            progresses[i]+=speeds[i]
            cnt+=1
            if progresses[i]>=100:
                lst.append(cnt)
                break
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i+1]=lst[i]
        else:
            continue
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    answer = list(count_dict.values())
    
    return answer