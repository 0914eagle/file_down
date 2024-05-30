
def check_safety(s, w):
    if w >= s:
        print("unsafe")
    else:
        print("safe")

# Read input from Standard Input
s, w = map(int, input().split())

# Check safety
check_safety(s, w)
