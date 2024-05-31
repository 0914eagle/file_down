
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def count_valid_permutations(n, a):
    total_permutations = factorial(n)
    valid_permutations = 0
    
    for x in range(1, 2001):
        candy_needed = x
        possible_permutations = 1
        
        for enemy_candy in a:
            if enemy_candy <= candy_needed:
                candy_needed -= enemy_candy
            else:
                possible_permutations = 0
                break
        
        valid_permutations += possible_permutations
    
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
print(*good_integers)
