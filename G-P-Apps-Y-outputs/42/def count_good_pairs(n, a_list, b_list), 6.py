
def count_good_pairs(n, a_list, b_list):
    good_pairs = 0
    count_a = {}
    count_b = {}
    
    for i in range(n):
        diff = a_list[i] - b_list[i]
        if diff in count_a:
            count_a[diff] += 1
        else:
            count_a[diff] = 1
    
    for i in range(n):
        diff = b_list[i] - a_list[i]
        if diff in count_b:
            count_b[diff] += 1
        else:
            count_b[diff] = 1
    
    for diff in count_a:
        if -diff in count_b:
            good_pairs += count_a[diff] * count_b[-diff]
    
    return good_pairs

# Read input
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# Print output
print(count_good_pairs(n, a_list, b_list))
```
