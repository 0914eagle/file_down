
def find_initial_sequences(n, sequence):
    sorted_sequence = sorted(sequence)
    
    increasing = []
    decreasing = []
    
    increasing_flag = True
    decreasing_flag = True
    
    for i in range(n):
        if not increasing and sorted_sequence[i] == sequence[i]:
            increasing.append(sequence[i])
        elif not decreasing and sorted_sequence[n-1-i] == sequence[i]:
            decreasing.append(sequence[i])
        else:
            increasing_flag = False
            decreasing_flag = False
            break
    
    if increasing_flag or decreasing_flag:
        if increasing and decreasing:
            print("YES")
            print(len(increasing))
            print(" ".join(map(str, increasing)))
            print(len(decreasing))
            print(" ".join(map(str, decreasing[::-1])))  # Reverse for decreasing order
        elif increasing:
            print("YES")
            print(len(increasing))
            print(" ".join(map(str, increasing)))
            print(0)
        else:
            print("YES")
            print(0)
            print(len(decreasing))
            print(" ".join(map(str, decreasing[::-1])))  # Reverse for decreasing order
    else:
        print("NO")

# Input processing
n = int(input())
sequence = list(map(int, input().split()))

find_initial_sequences(n, sequence)
```
