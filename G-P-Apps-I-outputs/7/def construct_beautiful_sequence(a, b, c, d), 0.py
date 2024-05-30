
def construct_beautiful_sequence(a, b, c, d):
    n = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        print("YES")
        if a >= b and b >= c and c >= d:
            seq = [0] * a + [1] * b + [2] * c + [3] * d
        elif a >= b and b >= c and c < d:
            seq = [0] * a + [1] * b + [3] * d + [2] * c
        elif a >= b and b < c and c >= d:
            seq = [0] * a + [2] * c + [1] * b + [3] * d
        elif a >= b and b < c and c < d:
            seq = [0] * a + [2] * c + [3] * d + [1] * b
        elif a < b and b >= c and c >= d:
            seq = [1] * b + [0] * a + [2] * c + [3] * d
        elif a < b and b >= c and c < d:
            seq = [1] * b + [0] * a + [3] * d + [2] * c
        elif a < b and b < c and c >= d:
            seq = [1] * b + [2] * c + [0] * a + [3] * d
        elif a < b and b < c and c < d:
            seq = [1] * b + [2] * c + [3] * d + [0] * a
        print(*seq)

a, b, c, d = map(int, input().split())
construct_beautiful_sequence(a, b, c, d)
```
