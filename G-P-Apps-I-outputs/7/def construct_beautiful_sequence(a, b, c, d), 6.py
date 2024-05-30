
def construct_beautiful_sequence(a, b, c, d):
    n = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        result = []
        if a >= b:
            result = [0, 1] * b
            a -= b
            result += [0] * a
        else:
            result = [1, 0] * a
            b -= a
            result += [1] * b

        if b >= c:
            result = result[:-1] + [2, 1] * c
            b -= c
            result += [2] * b
        else:
            result = result[:-1] + [1, 2] * b
            c -= b
            result += [1] * c

        if c >= d:
            result = result[:-1] + [3, 2] * d
            c -= d
            result += [3] * c
        else:
            result = result[:-1] + [2, 3] * c
            d -= c
            result += [2] * d

        print("YES")
        print(" ".join(map(str, result)))

# Input
a, b, c, d = map(int, input().split())
construct_beautiful_sequence(a, b, c, d)
```
