
from itertools import permutations

x = input()
digits = [int(digit) for digit in x]

permutations = permutations(digits)

for permutation in permutations:
    number = int(''.join([str(digit) for digit in permutation]))
    if number > int(x):
        print(number)
        break
else:
    print(0)

