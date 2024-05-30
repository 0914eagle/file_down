
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        result = []
        if a >= b:
            result.extend([0, 1] * b)
            a -= b
        else:
            result.extend([1, 0] * a)
            b -= a
        
        if b >= c:
            result.extend([1, 2] * c)
            b -= c
        else:
            result.extend([2, 1] * b)
            c -= b

        if c >= d:
            result.extend([2, 3] * d)
            c -= d
        else:
            result.extend([3, 2] * c)
            d -= c

        print("YES")
        print(*result)

# Example usage
construct_beautiful_sequence(2, 2, 2, 1)
construct_beautiful_sequence(1, 2, 3, 4)
construct_beautiful_sequence(2, 2, 2, 3)
```
