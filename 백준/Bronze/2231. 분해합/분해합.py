def sum_of_digit(n):
    digits=0
    while n>0:
        digits+=n%10
        n//=10
    return digits

found=False
n=int(input())
for i in range(1, n):
    if i+sum_of_digit(i)==n:
        print(i)
        found=True
        break
if not found:
    print(0)