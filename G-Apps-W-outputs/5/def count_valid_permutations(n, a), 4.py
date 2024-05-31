
def count_valid_permutations(n, a):
    fact = [1]
    for i in range(1, n + 1):
        fact.append(fact[-1] * i)
    
    def calculate_f(x):
        cnt = 0
        for i in range(1, n + 1):
            if a[i-1] <= x:
                cnt += fact[n-1] // fact[n-i] // fact[i-1]
        return cnt

    good_integers = []
    for x in range(1, 2001):
        if calculate_f(x) % p != 0:
            good_integers.append(x)
    
    return len(good_integers), good_integers

# Input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Output
result_count, result_values = count_valid_permutations(n, a)
print(result_count)
print(*result_values)
