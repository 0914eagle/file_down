
def wolf_attack(s, w):
    if w >= s:
        print("unsafe")
    else:
        print("safe")

# Input
s, w = map(int, input().split())

# Call the function
wolf_attack(s, w)
```
