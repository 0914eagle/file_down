
def get_pronunciation_of_hon(N):
    ones_place = N % 10

    if ones_place in [2, 4, 5, 7, 9]:
        return "hon"
    elif ones_place in [0, 1, 6, 8]:
        return "pon"
    elif ones_place == 3:
        return "bon"

# Read input
N = int(input())

# Get and print pronunciation of "本"
pronunciation = get_pronunciation_of_hon(N)
print(pronunciation)
```
