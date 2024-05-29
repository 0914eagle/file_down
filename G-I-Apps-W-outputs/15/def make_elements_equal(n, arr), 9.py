
def make_elements_equal(n, arr):
    min_val = min(arr)
    max_val = max(arr)
    diff = max_val - min_val

    if diff % 2 == 0:
        x = diff // 2
        for num in arr:
            if (num - min_val) % x != 0:
                return "NO"
        return "YES"
    return "NO"

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the output
print(make_elements_equal(n, arr))
