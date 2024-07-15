numS = 0
def phoneDesktop(x,y):
    if x == 0 and y == 0:
        return 0
    elif y >= 2 and x >= 7:
        
    else:
        phoneDesktop(x,y)








numOfCases = int(input())
for i in range(numOfCases):
    sumS = 0
    list1 = [int(x) for x in list if x.strip()]
    print(phoneDesktop(list1[0],list1[1]))