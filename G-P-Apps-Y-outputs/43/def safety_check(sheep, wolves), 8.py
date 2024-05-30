
def safety_check(sheep, wolves):
    if wolves >= sheep:
        print("unsafe")
    else:
        print("safe")

# Input
s, w = map(int, input().split())

# Perform safety check
safety_check(s, w)
```
