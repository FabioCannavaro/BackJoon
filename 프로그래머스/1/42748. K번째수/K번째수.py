def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        result=sorted(array[i-1:j])
        answer.append(result[k-1])
    return answer