
def solve(s):
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return s[::-1]
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
