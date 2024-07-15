def watermelon(x):
    if x % 2 == 0 and x > 2:
        for i in range(2, x, 2):
            if i % 2 == 0 and (x - i) % 2 == 0:
                return print('YES') 
    else: return print('NO') 
x = int(input())
watermelon(x)