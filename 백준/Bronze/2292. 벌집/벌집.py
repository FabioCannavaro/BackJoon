n = int(input())

if n == 1:
    print(1)
else:
    start = 2  
    end = 7  
    distance = 2  

    while True:
        if start <= n <= end:  
            print(distance)
            break

        start = end + 1 
        end = end + 6 * distance 
        distance += 1  