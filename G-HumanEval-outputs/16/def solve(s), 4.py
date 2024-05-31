
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
