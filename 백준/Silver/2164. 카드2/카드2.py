from collections import deque
def find_last_card(n):
    card = deque(range(1, n + 1))

    while len(card) > 1:
        card.popleft()
        card.append(card.popleft())

    return card[0]

n = int(input())
last_card = find_last_card(n)
print(last_card)

