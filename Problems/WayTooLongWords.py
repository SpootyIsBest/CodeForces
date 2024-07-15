def wayTooLong(word):
    if len(word) <= 10:
        print(word)
    else:
        print(f'{word[0]}{(len(word)-2)}{word[-1]}')


numOfCases = int(input())
for i in range(numOfCases):
    word = input()
    wayTooLong(word)