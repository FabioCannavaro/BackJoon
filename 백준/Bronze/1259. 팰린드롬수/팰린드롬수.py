def palindrome(n):
    if n==n[::-1]:
        print("yes")
    else:
        print("no")

while True:
    n=input()
    if n=="0":
        break
    else:
        result=palindrome(n)