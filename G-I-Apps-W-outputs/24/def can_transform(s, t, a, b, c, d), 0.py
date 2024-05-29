
def can_transform(s, t, a, b, c, d):
    count_s = {}
    count_t = {}
    
    for char in s[a-1:b]:
        count_s[char] = count_s.get(char, 0) + 1
        
    for char in t[c-1:d]:
        count_t[char] = count_t.get(char, 0) + 1
        
    if 'A' in count_t:
        count_s['C'] = count_s.get('C', 0) + count_t['A']
        count_t['A'] = 0
        
    if 'B' in count_t:
        count_s['A'] = count_s.get('A', 0) + count_t['B']
        count_t['B'] = 0
        
    if 'C' in count_t:
        count_s['B'] = count_s.get('B', 0) + count_t['C']
        count_t['C'] = 0
    
    return all(value >= 0 for value in (count_t.get('A', 0), count_t.get('B', 0), count_t.get('C', 0)))

# Parse input
s = input().strip()
t = input().strip()
q = int(input())

output = ""
for _ in range(q):
    a, b, c, d = map(int, input().split())
    output += '1' if can_transform(s, t, a, b, c, d) else '0'

print(output)
```
