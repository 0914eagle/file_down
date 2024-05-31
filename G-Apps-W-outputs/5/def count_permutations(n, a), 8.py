
def count_permutations(n, a):
    total_permutations = 1
    for i in range(1, n + 1):
        total_permutations *= i
    good_integers = []
    for x in range(1, total_permutations + 1):
        candies = x
        enemy_candies = sorted(a)
        valid_permutation = True
        for i in range(n):
            if candies >= enemy_candies[0]:
                candies -= enemy_candies.pop(0)
            else:
                valid_permutation = False
                break
        if valid_permutation:
            good_integers.append(x)
    
    good_count = 0
    good_numbers = []
    for x in good_integers:
        if total_permutations % x != 0:
            good_count += 1
            good_numbers.append(x)
    
    return good_count, good_numbers

# Input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Output
num_good, good_integers = count_permutations(n, a)
print(num_good)
for x in good_integers:
    print(x)
