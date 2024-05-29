
def construct_tree(n, d, k):
    if d >= n:
        print("NO")
    elif d == 1:
        if n > 2 or k < 2:
            print("NO")
        else:
            print("YES")
            for i in range(2, n+1):
                print("1", str(i))
    else:
        if k < 3:
            print("NO")
        else:
            print("YES")
            for i in range(2, d+2):
                print("1", str(i))
            parent = 1
            current = d + 2
            while current <= n:
                print(str(parent), str(current))
                current += 1
                for i in range(2, k):
                    if current <= n:
                        print(str(parent), str(current))
                        current += 1
                parent += 1

n, d, k = map(int, input().split())
construct_tree(n, d, k)
```
