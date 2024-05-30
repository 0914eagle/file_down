
def find_girls_name(N, boys, A, B):
    boys.sort()
    max_distance = -1
    girl_name = -1

    for i in range(A, B+1):
        min_distance = min([abs(i - boy) for boy in boys])
        if min_distance > max_distance:
            girl_name = i
            max_distance = min_distance

    return girl_name

# Input
N = int(input())
boys = list(map(int, input().split()))
A, B = map(int, input().split())

# Output
print(find_girls_name(N, boys, A, B))
```
