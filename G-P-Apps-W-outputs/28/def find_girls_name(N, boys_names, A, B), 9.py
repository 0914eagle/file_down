
def find_girls_name(N, boys_names, A, B):
    boys_names.sort()
    max_distance = 0
    girl_name = A
    for i in range(N):
        if i == 0:
            if boys_names[i] >= A:
                max_distance = boys_names[i] - A
                girl_name = A
            else:
                continue
        if i == N-1:
            if boys_names[i] <= B:
                distance = B - boys_names[i]
                if distance > max_distance:
                    max_distance = distance
                    girl_name = B
            break
        if boys_names[i] >= A and boys_names[i+1] <= B:
            distance = (boys_names[i+1]-boys_names[i]) // 2
            if distance > max_distance:
                max_distance = distance
                girl_name = boys_names[i] + distance
    return girl_name

# Input parsing
N = int(input())
boys_names = list(map(int, input().split()))
A, B = map(int, input().split())

# Call the function and output the result
print(find_girls_name(N, boys_names, A, B))
```
