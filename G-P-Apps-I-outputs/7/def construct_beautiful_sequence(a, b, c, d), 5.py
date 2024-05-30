
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        seq = []
        if a >= b:
            seq.extend([0, 1] * b + [0])
            a -= b
        else:
            seq.extend([1, 0] * a + [1])
            b -= a
        
        if b >= c:
            seq.extend([2, 1] * c + [2])
            b -= c
        else:
            seq.extend([1, 2] * b + [1])
            c -= b
        
        if c >= d:
            seq.extend([3, 2] * d + [3])
            c -= d
        else:
            seq.extend([2, 3] * c + [2])
            d -= c
        
        print("YES")
        print(" ".join(map(str, seq)))

# Input
a, b, c, d = map(int, input().split())
construct_beautiful_sequence(a, b, c, d)
```
