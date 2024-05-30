
def count_monotonic_renumerations(n, a):
    mod = 998244353
    freq = {}
    prev = {}
    ans = 1
    for i in range(n):
        if a[i] in freq:
            if i - prev[a[i]] != freq[a[i]]:
                return 0
        else:
            freq[a[i]] = 1
        prev[a[i]] = i

    for key in freq:
        ans = (ans * freq[key]) % mod

    return ans

# Input parsing
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(count_monotonic_renumerations(n, a))
```
