
def pronounce_pencils(n):
    ones_place = n % 10
    if ones_place in {2, 4, 5, 7, 9}:
        print("hon")
    elif ones_place in {0, 1, 6, 8}:
        print("pon")
    else:  # ones_place == 3
        print("bon")

# Read input
n = int(input().strip())
pronounce_pencils(n)
```
