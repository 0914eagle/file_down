
def sheep_safety(s, w):
    if w >= s:
        print("unsafe")
    else:
        print("safe")

# Input processing
s, w = map(int, input().split())
sheep_safety(s, w)
```
