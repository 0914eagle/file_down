
def make_good_string(n, s):
    # Function to check if a string is good
    def is_good_string(s):
        if len(s) % 2 != 0:
            return False
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                return False
        return True

    # Find the minimum number of characters to delete
    deletions = 0
    good_substr = ''
    for i in range(len(s)):
        if not is_good_string(good_substr + s[i]):
            deletions += 1
        else:
            good_substr += s[i]

    return deletions, good_substr

# Read input
n = int(input())
s = input()

# Get minimum deletions and resulting string
deletions, result = make_good_string(n, s)

# Print output
print(deletions)
print(result)
```
