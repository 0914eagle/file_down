
from itertools import permutations

def find_next_number(x):
    digits = [int(digit) for digit in str(x)]
    permutations_list = list(permutations(digits))
    sorted_permutations = sorted(permutations_list, key=lambda x: int(''.join(map(str, x))))
    for permutation in sorted_permutations:
        number = int(''.join(map(str, permutation)))
        if number > x:
            return number
    return 0

x = int(input())
result = find_next_number(x)
print(result)

