
def construct_string(n, k, t):
    # Construct a repeating string of length n * k
    base_string = t * k
    
    # Find the longest prefix of the base string that matches the suffix of t
    p = [0] * (n + 1)
    j = 0
    for i in range(2, n + 1):
        while j > 0 and t[j] != t[i - 1]:
            j = p[j]
        if t[j] == t[i - 1]:
            j += 1
        p[i] = j
    
    # Calculate the length of the repeating part of the string
    repeating_length = n - p[-1]
    
    # Construct the final string by taking the repeating part and adding extra characters as needed
    final_string = base_string[:n - repeating_length] + base_string
    return final_string

# Read input
n, k = map(int, input().split())
t = input().strip()

# Call the function and print the result
result = construct_string(n, k, t)
print(result)
