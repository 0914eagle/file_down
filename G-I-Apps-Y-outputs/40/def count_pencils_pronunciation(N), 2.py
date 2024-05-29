
def count_pencils_pronunciation(N):
    ones_place = N % 10
    
    if ones_place in [2, 4, 5, 7, 9]:
        print("hon")
    elif ones_place in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

# Input
N = int(input())

# Call the function with the input
count_pencils_pronunciation(N)
```
