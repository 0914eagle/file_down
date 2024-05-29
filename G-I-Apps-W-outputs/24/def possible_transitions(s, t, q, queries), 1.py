
def possible_transitions(s, t, q, queries):
    def can_transform(s, t):
        while len(s) > 0:
            if len(s) < len(t):
                return False
            for i in range(len(t)):
                if s[i] == t[i]:
                    continue
                if s[i] == 'A' and t[i] == 'C':
                    s = s[:i] + 'CC' + s[i+1:]
                elif s[i] == 'B' and t[i] == 'C':
                    s = s[:i] + 'A' + s[i+1:]
                elif s[i] == 'A' and t[i] == 'B':
                    s = s[:i] + 'C' + s[i+1:]
                elif s[i:i+3] == 'AAA':
                    s = s[:i] + s[i+3:]
                else:
                    return False
                break
        return True

    result = ""
    for i in range(q):
        a, b, c, d = queries[i]
        if can_transform(s[a-1:b], t[c-1:d]):
            result += '1'
        else:
            result += '0'
    return result

# Reading input
s = input().strip()
t = input().strip()
q = int(input().strip())
queries = []
for _ in range(q):
    a, b, c, d = map(int, input().strip().split())
    queries.append((a, b, c, d))

# Calling the function with input
output = possible_transitions(s, t, q, queries)
print(output)
```
