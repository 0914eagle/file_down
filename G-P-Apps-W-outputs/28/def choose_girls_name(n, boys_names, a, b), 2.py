
def choose_girls_name(n, boys_names, a, b):
    max_distance = -1
    chosen_name = -1
    
    for x in range(a, b+1, 2):
        min_distance = min([abs(x - p) for p in boys_names])
        if min_distance > max_distance:
            max_distance = min_distance
            chosen_name = x
    
    return chosen_name

# Input
n = int(input())
boys_names = list(map(int, input().split()))
a, b = map(int, input().split())

# Output
print(choose_girls_name(n, boys_names, a, b))
```
