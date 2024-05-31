
def solve(s):
    result = ''
    has_letter = False
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    if not has_letter:
        result = result[::-1]

    return result

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))  # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
