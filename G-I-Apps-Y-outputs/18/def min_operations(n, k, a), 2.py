
def min_operations(n, k, a):
    a.sort()
    unique_elements = set(a)
    possible_numbers = []
    for num in unique_elements:
        count = a.count(num)
        possible_numbers.append((num, count))
    possible_numbers.sort(key=lambda x: (x[1], x[0]))

    min_operations = float('inf')
    for i in range(len(possible_numbers)):
        target_num = possible_numbers[i][0]
        target_count = possible_numbers[i][1]
        total_operations = 0
        for j in range(len(possible_numbers)):
            current_num, current_count = possible_numbers[j]
            if current_count < target_count:
                continue
            operations = 0
            while current_num < target_num:
                current_num *= 2
                operations += 1
            total_operations += operations * current_count
        min_operations = min(min_operations, total_operations)
    
    return min_operations

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(min_operations(n, k, a))
```
