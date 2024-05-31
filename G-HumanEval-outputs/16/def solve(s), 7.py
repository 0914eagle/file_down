
def solve(s):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_s = ""
    
    for char in s:
        if char.isalpha():
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char
    
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return new_s

# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
