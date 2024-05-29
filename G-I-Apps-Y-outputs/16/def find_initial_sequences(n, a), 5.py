
def find_initial_sequences(n, a):
    increasing = []
    decreasing = []
    for i in range(n):
        if len(increasing) == 0 or a[i] > increasing[-1]:
            increasing.append(a[i])
        elif len(decreasing) == 0 or a[i] < decreasing[-1]:
            decreasing.append(a[i])
        else:
            print("NO")
            return
    
    print("YES")
    print(len(increasing))
    print(" ".join(map(str, increasing)))
    print(len(decreasing))
    print(" ".join(map(str, decreasing[::-1]))

# Read input
n = int(input())
a = list(map(int, input().split()))

# Call function
find_initial_sequences(n, a)
```
