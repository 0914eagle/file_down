
def max_boxers_team(n, weights):
    freq_dict = {}
    for weight in weights:
        freq_dict[weight] = freq_dict.get(weight, 0) + 1
    
    max_team = 0
    for weight in freq_dict:
        max_team += min(freq_dict[weight], freq_dict[weight+1])

    return max_team

# Input
n = int(input())
weights = list(map(int, input().split()))

# Output
print(max_boxers_team(n, weights))
```
