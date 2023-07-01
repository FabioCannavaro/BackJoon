def count_cable(cable, length):
    cnt=0
    for i in cable:
        cnt+=i//length
    return cnt
def binary_cable(cable, k, low, high):
    result = 0
    while low <= high:
        mid = (low + high) // 2
        count = count_cable(cable, mid)
        if count >= k:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
n, k=map(int, input().split())
cable=[]
for i in range(n):
    num=int(input())
    cable.append(num)
max_length = max(cable)
res=binary_cable(cable, k, 1, max_length)
print(res)