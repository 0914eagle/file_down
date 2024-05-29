
def find_sequences(n, a):
    increasing = []
    decreasing = []
    last_inc = -1
    last_dec = float('inf')
    
    for num in a:
        if num > last_inc:
            increasing.append(num)
            last_inc = num
        elif num < last_dec:
            decreasing.append(num)
            last_dec = num
        else:
            print("NO")
            return
    
    print("YES")
    print(len(increasing))
    print(' '.join(map(str, increasing)))
    print(len(decreasing))
    print(' '.join(map(str, decreasing)))

# Input parsing
n = int(input())
a = list(map(int, input().split()))

find_sequences(n, a)
```
