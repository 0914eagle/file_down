
def max_objects_packed(n, m, k, a):
    max_objects = 0
    for i in range(n):
        count = 1
        space_left = k
        j = i
        while j < n and space_left >= a[j]:
            space_left -= a[j]
            j += 1
            count += 1
        max_objects = max(max_objects, count - 1)
    return max_objects

# Read input
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_objects_packed(n, m, k, a))
```
