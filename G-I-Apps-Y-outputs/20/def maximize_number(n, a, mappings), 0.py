
def maximize_number(n, a, mappings):
    best_mapping = {str(i+1): str(mappings[i]) for i in range(9)}
    
    # Function to apply mapping to a subsegment
    def apply_mapping(seg):
        result = []
        for digit in seg:
            result.append(best_mapping[digit])
        return "".join(result)
    
    # Find the maximum possible number
    max_number = a
    for i in range(n):
        for j in range(i, n):
            new_number = list(a)
            new_number[i:j+1] = apply_mapping(new_number[i:j+1])
            new_number = int("".join(new_number))
            if new_number > int(max_number):
                max_number = str(new_number)
    
    return max_number

# Read input
n = int(input())
a = input().strip()
mappings = list(map(int, input().split()))

# Print output
print(maximize_number(n, a, mappings))
```
