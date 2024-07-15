z = 0
i = 0
numOfCases = int(input())
while i < numOfCases:
    while ('X++' == input() or '++X' == input()) and i < numOfCases:
        z += 1
        i += 1
    while ('X--' == input() or '--X' == input()) and i < numOfCases:
        z -= 1
        i += 1
print(z) 