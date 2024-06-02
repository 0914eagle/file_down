
def minimize_ternary_string(s):
    s = list(s)
    n = len(s)
    
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            j = i
            while j >= 0 and s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                j -= 1
    
    return ''.join(s)

# Read input
s = input().strip()

# Call the function and print the result
print(minimize_ternary_string(s))
