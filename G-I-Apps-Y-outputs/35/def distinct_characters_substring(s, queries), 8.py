
def distinct_characters_substring(s, queries):
    result = []
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            substring = s[l-1:r]
            unique_chars_count = len(set(substring))
            result.append(unique_chars_count)
    
    return result

# Reading input
s = input().strip()
q = int(input())
queries = []
for _ in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        queries.append((1, int(query[1]), query[2]))
    elif query[0] == '2':
        queries.append((2, int(query[1]), int(query[2])))

# Calculating and printing the results
output = distinct_characters_substring(s, queries)
for ans in output:
    print(ans)
