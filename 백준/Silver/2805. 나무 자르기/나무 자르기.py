N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
while start<=end:
    mid = (start+end) // 2
    cut = 0
    for i in tree:
        if i > mid:
            cut += i - mid

    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
        