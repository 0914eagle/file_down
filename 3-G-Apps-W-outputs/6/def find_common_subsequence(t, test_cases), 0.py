
def find_common_subsequence(t, test_cases):
    def is_subsequence(arr1, arr2):
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                i += 1
            j += 1
        return i == len(arr1)

    results = []
    for _ in range(t):
        n, m, a, b = test_cases[_]
        found = False
        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    found = True
                    result = [a[i]]
                    break
            if found:
                break

        if found:
            results.append(("YES", 1, result))
        else:
            results.append(("NO", 0, []))

    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Find common subsequences
results = find_common_subsequence(t, test_cases)

# Output results
for result in results:
    print(result[0])
    if result[0] == "YES":
        print(result[1], *result[2])
