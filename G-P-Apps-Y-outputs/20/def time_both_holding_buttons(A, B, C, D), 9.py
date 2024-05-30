
def time_both_holding_buttons(A, B, C, D):
    start = max(A, C)
    end = min(B, D)
    
    if end > start:
        return end - start
    else:
        return 0

A, B, C, D = map(int, input().split())
print(time_both_holding_buttons(A, B, C, D))
```
