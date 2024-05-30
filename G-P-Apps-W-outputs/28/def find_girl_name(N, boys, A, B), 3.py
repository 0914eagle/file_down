
def find_girl_name(N, boys, A, B):
    boys.sort()
    max_distance = 0
    girl_name = A
    for i in range(A, B + 1):
        min_distance = min([abs(i - boy) for boy in boys])
        if min_distance > max_distance:
            max_distance = min_distance
            girl_name = i
    return girl_name

# Read input
N = int(input())
boys = list(map(int, input().split()))
A, B = map(int, input().split())

# Find the name for the little girl
girl_name = find_girl_name(N, boys, A, B)

# Output the result
print(girl_name)
```
