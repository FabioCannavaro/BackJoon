a, b, v=map(int, input().split())
cnt = (v - b) // (a - b)
if (v - b) % (a - b) != 0:
    cnt += 1
print(cnt)