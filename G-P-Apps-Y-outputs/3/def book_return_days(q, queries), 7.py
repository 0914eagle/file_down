
def book_return_days(q, queries):
    result = []
    
    for query in queries:
        n = query[0]
        p = query[1]

        book_returned_days = [0] * n

        for i in range(n):
            visited = set()
            count = 0
            j = i
            while p[j] not in visited:
                visited.add(j)
                j = p[j] - 1
                count += 1
            book_returned_days[i] = count

        result.append(book_returned_days)

    return result

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

# Call the function and print the output
output = book_return_days(q, queries)
for res in output:
    print(' '.join(map(str, res)))
```
