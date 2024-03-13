def solution(numbers):
    answer = ''
    lst=[]
    for i in numbers:
        lst.append(str(i))
    lst.sort(key=lambda x: x*3, reverse=True)
    answer=''.join(lst)
    if answer[0]=='0':
        return '0'
    else:
        return answer
