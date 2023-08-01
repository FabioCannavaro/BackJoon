def remote_control(broke_buttons):
    all_buttons = set(range(10))
    return all_buttons - set(broke_buttons)

def check_possible_channel(channel, available_buttons):
    for digit in str(channel):
        if int(digit) not in available_buttons:
            return False
    return True

def closest_channel(target, available_buttons):
    min_button_press = abs(target - 100)

    for channel in range(1000001):
        if check_possible_channel(channel, available_buttons):
            button_press = abs(target - channel) + len(str(channel))
            min_button_press = min(min_button_press, button_press)

    return min_button_press

def main():
    try:
        while True:
            N = int(input())
            broken_buttons_count = int(input())
            broken_buttons=[]
            if broken_buttons_count > 0:
                broken_buttons = list(map(int, input().split()))
            available_buttons = remote_control(broken_buttons)
            result=closest_channel(N, available_buttons)
            print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
