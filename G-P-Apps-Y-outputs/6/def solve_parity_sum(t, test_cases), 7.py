
def solve_parity_sum(t, test_cases):
    def find_parity_sum(n, k):
        if n % 2 != k % 2 or n < k:
            return None
        
        if k == 1:
            return [n]
        
        if n % 2 == 0:
            return [n // 2] * (k - 1) + [n // 2]
        else:
            if k == 2:
                return None
            return [1] * (k - 1) + [n - k + 1]
    
    results = []
    for n, k in test_cases:
        result = find_parity_sum(n, k)
        if result:
            results.append((True, result))
        else:
            results.append((False, None))
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    test_cases.append((n, k))

# Solve the problem
results = solve_parity_sum(t, test_cases)

# Output results
for result in results:
    if result[0]:
        print("YES")
        print(*result[1])
    else:
        print("NO")
