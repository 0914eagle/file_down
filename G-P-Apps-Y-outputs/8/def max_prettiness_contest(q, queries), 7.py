
def max_prettiness_contest(q, queries):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def max_prettiness(nums):
        nums.sort(reverse=True)
        n = len(nums)

        if n <= 2:
            return sum(nums)

        max_prettiness = 0
        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) == 1:
                    max_prettiness = max(max_prettiness, nums[i] + nums[j])

        return max_prettiness

    results = []
    for query in queries:
        n = query[0]
        nums = query[1]
        results.append(max_prettiness(nums))

    return results

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    nums = list(map(int, input().split()))
    queries.append((n, nums))

# Get the results
results = max_prettiness_contest(q, queries)

# Output results
for result in results:
    print(result)
```
