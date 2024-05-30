
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        res = []
        if a >= b:
            res.extend([0, 1] * b)
            a -= b
        else:
            res.extend([1, 0] * a)
            b -= a
        
        if b >= c:
            res.extend([1, 2] * c)
            b -= c
        else:
            res.extend([2, 1] * b)
            c -= b
        
        if c >= d:
            res.extend([2, 3] * d)
            c -= d
        else:
            res.extend([3, 2] * c)
            d -= c
        
        print("YES")
        print(" ".join(map(str, res)))

# Input
a, b, c, d = map(int, input().split())
construct_beautiful_sequence(a, b, c, d)
```
