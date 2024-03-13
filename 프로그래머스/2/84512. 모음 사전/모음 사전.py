from itertools import product
def solution(word):
    answer = 0
    all_words=[]
    arr=['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        all_words.extend([''.join(w) for w in product(arr, repeat=i)])
    all_words.sort()

    answer = all_words.index(word) + 1
    return answer