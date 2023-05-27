pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [1,23,2,2,8, 3.9]
numbers.sort()


def dotheShit(numbers):
    for i in range(len(numbers)):
        print(numbers[i])


dotheShit(numbers)

names = ["Graham","John","Terry","eric","terry","michael"]
names.sort(key=str.casefold)
print(names)
