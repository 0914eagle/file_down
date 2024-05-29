
def distinct_characters_in_substring(s, queries):
    for query in queries:
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos-1] + c + s[pos:]
        elif query[0] == 2:
            l, r = query[1], query[2]
            substring = s[l-1:r]
            distinct_chars = len(set(substring))
            print(distinct_chars)

# Sample Input Processing
s = "abacaba"
q = 5
queries = [
    (2, 1, 4),
    (1, 4, 'b'),
    (1, 5, 'b'),
    (2, 4, 6),
    (2, 1, 7)
]

distinct_characters_in_substring(s, queries)
```
