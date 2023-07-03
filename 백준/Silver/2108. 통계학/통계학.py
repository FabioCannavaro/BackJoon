import sys
def arithmetic_mean(numbers, n):
    total = sum(numbers)
    
    return print(round(total / n)) 

def median_value(numbers):
    numbers.sort()
    mid=(len(numbers)-1)//2
    
    return print(numbers[mid])

def find_mode(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1    
    mode_freq = max(freq_dict.values())
        
    modes = [num for num, freq in freq_dict.items() if freq == mode_freq]
    modes.sort()
    return print(modes[1] if len(modes) > 1 else modes[0])

def find_range(numbers):
    top=max(lst)
    bot=min(lst)
    return print(top-bot)

n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    num=int(sys.stdin.readline())
    lst.append(num)
arithmetic_mean(lst, n)
median_value(lst)
find_mode(lst)
find_range(lst)