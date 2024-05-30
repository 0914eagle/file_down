
def distinct_characters(s, queries):
    unique_chars = []
    result = []
    
    for query in queries:
        if query[0] == 1:  # Replace character
            s = s[:query[1] - 1] + query[2] + s[query[1]:]
        elif query[0] == 2:  # Calculate distinct characters
            sub = s[query[1]-1:query[2]]
            unique_chars = set(sub)
            result.append(len(unique_chars))
    
    return result

# Input parsing
s = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    queries.append(list(map(str, input().strip().split())))

# Call the function and print the results
results = distinct_characters(s, queries)
for res in results:
    print(res)
```
