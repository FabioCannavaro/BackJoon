import sys
class StatisticsCalculator:
    def __init__(self, numbers):
        self.numbers=numbers
        
    def arithmetic_mean(self):
        total = sum(self.numbers)

        return round(total / len(self.numbers))

    def median_value(self):
        self.numbers.sort()
        mid=(len(self.numbers)-1)//2

        return self.numbers[mid]

    def find_mode(self):
        freq_dict = {}
        for num in self.numbers:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        mode_freq = max(freq_dict.values())

        modes = [num for num, freq in freq_dict.items() if freq == mode_freq]
        modes.sort()
        return modes[1] if len(modes) > 1 else modes[0]

    def find_range(self):
        top=max(self.numbers)
        bot=min(self.numbers)
        return abs(top-bot)

n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    num=int(sys.stdin.readline())
    lst.append(num)
calculator = StatisticsCalculator(lst)

print(calculator.arithmetic_mean())
print(calculator.median_value())
print(calculator.find_mode())
print(calculator.find_range())