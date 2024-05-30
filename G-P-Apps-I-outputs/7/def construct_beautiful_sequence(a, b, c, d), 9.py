
def construct_beautiful_sequence(a, b, c, d):
    total = a + b + c + d
    if abs(a - b) > 1 or abs(b - c) > 1 or abs(c - d) > 1:
        print("NO")
    else:
        result = []
        if a >= b:
            for i in range(a):
                result.append(0)
                if b > 0:
                    result.append(1)
                    b -= 1
            for i in range(b):
                result.append(1)
                if c > 0:
                    result.append(2)
                    c -= 1
            for i in range(c):
                result.append(2)
                if d > 0:
                    result.append(3)
                    d -= 1
        else:
            for i in range(b):
                result.append(1)
                if a > 0:
                    result.insert(0, 0)
                    a -= 1
            for i in range(a):
                result.insert(0, 0)
                if c > 0:
                    result.append(2)
                    c -= 1
            for i in range(c):
                result.append(2)
                if d > 0:
                    result.append(3)
                    d -= 1
        print("YES")
        print(*result)

# Input example
a, b, c, d = 2, 2, 2, 1
construct_beautiful_sequence(a, b, c, d)
```
