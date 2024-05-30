
def construct_beautiful_sequence(a, b, c, d):
    if abs(a - b) <= 1 and abs(c - d) <= 1:
        if a > b:
            seq = [0, 1] * b + [0] * (a - b)
        elif b > a:
            seq = [1, 0] * a + [1] * (b - a)
        elif c > d:
            seq = [2, 3] * d + [2] * (c - d)
        elif d > c:
            seq = [3, 2] * c + [3] * (d - c)
        else:
            seq = [0, 1] * a + [2, 3] * c
        return "YES\n" + ' '.join(map(str, seq))
    else:
        return "NO"

# Input parsing
a, b, c, d = map(int, input().split())

# Call the function and print the result
print(construct_beautiful_sequence(a, b, c, d))
```
