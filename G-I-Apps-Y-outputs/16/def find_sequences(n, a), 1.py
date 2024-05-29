
def find_sequences(n, a):
    increasing_sequence = []
    decreasing_sequence = []
    
    if n == 1:
        print("YES")
        print("1")
        print(a[0])
        print("0")
        print("")
        return
    
    increasing = True
    decreasing = True
    
    for i in range(1, n):
        if a[i] == a[i-1]:
            increasing = False
            decreasing = False
        elif a[i] > a[i-1]:
            decreasing = False
        else:
            increasing = False
            
    if not increasing and not decreasing:
        print("NO")
        return
    
    if increasing:
        increasing_sequence = a
    else:
        increasing_sequence = sorted(a)

    if decreasing:
        decreasing_sequence = a
    else:
        decreasing_sequence = sorted(a, reverse=True)
    
    print("YES")
    print(len(increasing_sequence))
    print(" ".join(map(str, increasing_sequence)))
    print(len(decreasing_sequence))
    print(" ".join(map(str, decreasing_sequence)))


n = int(input())
a = list(map(int, input().split()))

find_sequences(n, a)
```
