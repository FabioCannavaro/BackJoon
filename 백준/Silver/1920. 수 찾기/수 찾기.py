def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return False
if __name__=='__main__':
    num1=int(input())
    f_num=list(map(int, input().split()))
    f_num.sort()
    num2=int(input())
    s_num=list(map(int, input().split()))
    for i in s_num:
        if binary_search(f_num, i):
            print(1)
        else:
            print(0)