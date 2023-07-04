def black_jack(m, card):
    closest_sum = 0
    n = len(card)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = card[i] + card[j] + card[k]
                if current_sum <= m and current_sum > closest_sum:
                    closest_sum = current_sum

    return closest_sum

n, m = map(int, input().split())
card=list(map(int, input().split()))

result = black_jack(m, card)
print(result)