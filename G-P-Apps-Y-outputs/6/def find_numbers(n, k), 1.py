
def find_numbers(n, k):
    if n % 2 != k % 2 or n < k:
        return None
    
    quotient = n // k
    if quotient % 2 == 0:
        return [quotient] * k
    elif k % 2 == 0:
        return [quotient - 1] + [2] * (k - 1)
    else:
        return [quotient - 2] + [2] * (k - 1)

def solve_test_cases(test_cases):
    results = []
    for n, k in test_cases:
        numbers = find_numbers(n, k)
        if numbers is not None:
            results.append("YES\n" + " ".join(map(str, numbers)))
        else:
            results.append("NO")
    return results

t = int(input())
test_cases = [list(map(int, input().split())) for _ in range(t)]

output = solve_test_cases(test_cases)
for result in output:
    print(result)
```
