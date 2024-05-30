
def count_possible_strings(n, q, operations):
    def helper(curr_str):
        if len(curr_str) == 1:
            return 1
        
        count = 0
        for a, b in operations:
            if curr_str[:2] == a:
                new_str = b + curr_str[2:]
                count += helper(new_str)
        
        return count
    
    count = 0
    initial_strings = [''.join(x) for x in product('abcdef', repeat=n)]

    for s in initial_strings:
        count += helper(s)

    return count

n, q = map(int, input().split())
operations = [input().split() for _ in range(q)]

result = count_possible_strings(n, q, operations)
print(result)
```
