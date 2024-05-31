
def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
