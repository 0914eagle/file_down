
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        res = []
        if a >= b:
            res += [0, 1] * b + [0] * (a - b)
        else:
            res += [1, 0] * a + [1] * (b - a)
        
        if b >= c:
            res += [1, 2] * c + [1] * (b - c)
        else:
            res += [2, 1] * b + [2] * (c - b)
        
        if c >= d:
            res += [2, 3] * d + [2] * (c - d)
        else:
            res += [3, 2] * c + [3] * (d - c)
        
        print("YES")
        print(" ".join(map(str, res)))

# Example usage
construct_beautiful_sequence(2, 2, 2, 1)
construct_beautiful_sequence(1, 2, 3, 4)
construct_beautiful_sequence(2, 2, 2, 3)
```
