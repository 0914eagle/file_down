
def find_girl_name(N, boys, A, B):
    sorted_boys = sorted(boys)
    max_distance = 0
    best_name = A
    for x in range(A, B+1, 2):
        min_distance = min([abs(x - boy) for boy in sorted_boys])
        if min_distance > max_distance:
            max_distance = min_distance
            best_name = x
    return best_name

# Input
N = int(input())
boys = list(map(int, input().split()))
A, B = map(int, input().split())

# Output
print(find_girl_name(N, boys, A, B))
```
