
def solve(s):
    letters = [c for c in s if c.isalpha()]
    if len(letters) == 0:
        return s[::-1]
    else:
        return ''.join([c.lower() if c.isupper() else c.upper() for c in s])

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
