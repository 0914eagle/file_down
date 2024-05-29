
def calculate_min_distances(n, x_list, v_list):
    total_distance = 0
    total_x = sum(x_list)
    
    for i in range(n):
        for j in range(i+1, n):
            if v_list[i] != v_list[j]:
                t_intersect = (x_list[j] - x_list[i]) / (v_list[i] - v_list[j])
                if t_intersect > 0:
                    x_intersect = x_list[i] + t_intersect * v_list[i]
                    min_distance = abs(x_intersect - x_list[i]) + abs(x_intersect - x_list[j])
                    total_distance += min_distance
                else:
                    total_distance += abs(x_list[i] - x_list[j])
    
    return total_distance

# Read input values
n = int(input())
x_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

# Calculate and print the result
result = calculate_min_distances(n, x_list, v_list)
print(result)
```
