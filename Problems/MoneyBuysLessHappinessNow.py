def lessHappines(months,salary,list):
    mySavings = 0
    mwh = 0
    for i in range(months):
        if mySavings >= list[i]:
            mwh += 1
            mySavings -= list[i]
        mySavings += salary

    return print(mwh)

numOfMonths = int(input())
for i in range(numOfMonths):
    list = list(input())
    list1 = [int(x) for x in list if x.strip()]
    lessHappines(int(list1[0]),int(list1[1]),list1[2:])