
def find_girls_name(N, boys_names, A, B):
    max_distance = 0
    girl_name = A
    for i in range(A, B+1):
        min_distance = min([abs(i - x) for x in boys_names])
        if min_distance > max_distance:
            max_distance = min_distance
            girl_name = i
    return girl_name

# Input
N = int(input())
boys_names = list(map(int, input().split()))
A, B = map(int, input().split())

# Output
print(find_girls_name(N, boys_names, A, B))
```
