def nono_sqrt(min_val, max_val):

    check = [0] * (max_val - min_val + 1)
    for i in range(2, int(max_val**0.5)+1):
        sqrt_num=i*i
        start = (((min_val-1)//sqrt_num) + 1) * sqrt_num
        for j in range(start, max_val+1, sqrt_num):
            check[j-min_val]=1
    return check.count(0)

n, m = map(int, input().split())

print(nono_sqrt(n, m))