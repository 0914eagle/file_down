
def find_minimum_length_string(n, k, t):
    repeated = k - 1
    common_prefix = ''
    for i in range(1, n):
        if t[:i] == t[n - i:]:
            common_prefix = t[:i]
    
    result = t + (t[n - len(common_prefix):] * repeated)
    return result

# Input reading
n, k = map(int, input().split())
t = input().strip()

# Call the function and print the result
print(find_minimum_length_string(n, k, t))
