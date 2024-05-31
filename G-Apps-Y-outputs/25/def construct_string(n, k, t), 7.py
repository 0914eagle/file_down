
def construct_string(n, k, t):
    repeated_str = 'a' * (n - 1)
    s = t + repeated_str * (k - 1)
    return s

# Input processing
n, k = map(int, input().split())
t = input().strip()

# Call the function and print the result
result = construct_string(n, k, t)
print(result)
