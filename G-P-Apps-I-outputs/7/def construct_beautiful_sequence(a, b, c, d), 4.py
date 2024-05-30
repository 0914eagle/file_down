
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    sequence = []

    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        return "NO"
    
    if a > b:
        sequence.extend([0, 1] * b)
        a -= b
        b = 0
    else:
        sequence.extend([1, 0] * a)
        b -= a
        a = 0
    
    if b > c:
        sequence.extend([1, 2] * c)
        b -= c
        c = 0
    else:
        sequence.extend([2, 1] * b)
        c -= b
        b = 0
    
    if c > d:
        sequence.extend([2, 3] * d)
        c -= d
        d = 0
    else:
        sequence.extend([3, 2] * c)
        d -= c
        c = 0
    
    if a == b == c == d == 0:
        return "YES\n" + " ".join(map(str, sequence))
    else:
        return "NO"

# Input parsing
a, b, c, d = map(int, input().split())
print(construct_beautiful_sequence(a, b, c, d))
```
