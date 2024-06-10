
from itertools import permutations

x = input()

def find_next_permutation(num):
    digits = [int(d) for d in str(num)]
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            break
    else:
        return 0
    j = len(digits) - 1
    while digits[j] <= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = reversed(digits[i:])
    next_permutation = int(''.join(map(str, digits)))
    return next_permutation

print(find_next_permutation(x))

