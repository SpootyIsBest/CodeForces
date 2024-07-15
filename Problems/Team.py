s = 0
numOfCases = int(input())
for i in range(numOfCases):
    list1 = list(input())
    list1 = [int(x) for x in list1 if x.strip()]
    if (list1[0] + list1[1] + list1[2]) >= 2:
        s+=1
print(s)