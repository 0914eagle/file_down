
from itertools import permutations

def find_next_number(num):
    digits = [int(digit) for digit in str(num)]
    permutations_list = permutations(digits)
    next_number = None
    for permutation in permutations_list:
        permutation_number = int("".join(map(str, permutation)))
        if permutation_number > num:
            next_number = permutation_number
            break
    return next_number

num = int(input())
next_number = find_next_number(num)
print(next_number if next_number is not None else 0)

