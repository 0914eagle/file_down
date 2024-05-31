
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    
    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    
    return result

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
