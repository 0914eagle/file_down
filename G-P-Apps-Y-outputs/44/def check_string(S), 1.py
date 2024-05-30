
def check_string(S):
    if S[0] != 'A':
        return 'WA'
    if not S[2:-1].count('C') == 1:
        return 'WA'
    if not all(letter.islower() for letter in S[1:] if letter not in {'A', 'C'}):
        return 'WA'
    return 'AC'

# Read input from Standard Input
S = input().strip()

# Check if the string satisfies the conditions
result = check_string(S)
print(result)
```
