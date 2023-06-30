def is_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

while True:
    n = input()
    if n == "0":
        break
    else:
        if is_palindrome(n):
            print("yes")
        else:
            print("no")
