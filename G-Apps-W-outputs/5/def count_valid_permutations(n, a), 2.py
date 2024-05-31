
def count_valid_permutations(n, a):
    total_permutations = 1
    for i in range(1, n + 1):
        total_permutations *= i

    valid_permutations = 0
    for x in range(1, total_permutations + 1):
        candies = x
        valid = True
        for i in range(n, 0, -1):
            if candies < a[i - 1]:
                valid = False
                break
            candies += 1
        if valid:
            valid_permutations += 1

    return valid_permutations

def find_good_integers(n, p, a):
    good_integers = []
    for x in range(1, 2001):
        if count_valid_permutations(n, a) % p != 0:
            good_integers.append(x)

    return len(good_integers), good_integers

# Input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Output
count, good_integers = find_good_integers(n, p, a)
print(count)
print(" ".join(map(str, good_integers)))
