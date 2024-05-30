
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        result = []
        if a >= b:
            result.extend([0, 1] * b)
            a -= b
            result.extend([0] * a)
        else:
            result.extend([1, 0] * a)
            b -= a
            result.extend([1] * b)

        if c >= d:
            result.extend([2, 3] * d)
            c -= d
            result.extend([2] * c)
        else:
            result.extend([3, 2] * c)
            d -= c
            result.extend([3] * d)

        print("YES")
        print(*result)

# Input example: 2 2 2 1
a, b, c, d = map(int, input().split())
construct_beautiful_sequence(a, b, c, d)
```
