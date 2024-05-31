
def count_valid_permutations(n, a):
    cnt = 0
    for x in range(1, 2001):
        valid = True
        for i in range(1, n + 1):
            if x < a[i - 1]:
                valid = False
                break
        if valid:
            cnt += 1
    return cnt

def is_good_integer(n, p, a):
    good_integers = []
    for x in range(1, n + 1):
        f_x = count_valid_permutations(n, [x] + a)  # Add x to the beginning of the array
        if f_x % p != 0:
            good_integers.append(x)

    num_good_integers = len(good_integers)
    return num_good_integers, good_integers

# Input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Output
num_good_integers, good_integers = is_good_integer(n, p, a)
print(num_good_integers)
for x in good_integers:
    print(x)
