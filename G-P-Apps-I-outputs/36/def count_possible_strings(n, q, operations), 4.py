
def count_possible_strings(n, q, operations):
    def compress_string(s):
        while len(s) > 1:
            compressed = False
            for a, b in operations:
                if s.startswith(a):
                    s = b + s[2:]
                    compressed = True
                    break
            if not compressed:
                break
        return s

    def generate_strings(length, prefix=''):
        if length == 0:
            return [prefix]
        
        strings = []
        for char in 'abcdef':
            strings += generate_strings(length - 1, prefix + char)
        return strings

    possible_strings = set()
    for s in generate_strings(n):
        if compress_string(s) == 'a':
            possible_strings.add(s)

    return len(possible_strings)

# Input
n, q = map(int, input().split())
operations = [tuple(input().split()) for _ in range(q)]

# Output
print(count_possible_strings(n, q, operations))
```
