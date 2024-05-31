
def solve(s):
    letters = ''.join(c for c in s if c.isalpha())
    if not letters:
        return s[::-1]
    else:
        result = ''
        for c in s:
            if c.isalpha():
                if c.islower():
                    result += c.upper()
                else:
                    result += c.lower()
            else:
                result += c
        return result

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))  # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
