from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card_counter = Counter(cards)

for num in check:
    print(card_counter[num], end=' ')