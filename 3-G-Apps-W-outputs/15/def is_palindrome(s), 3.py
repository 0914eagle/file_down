
def is_palindrome(s):
    return s == s[::-1]

def rearrange_string(s):
    if is_palindrome(s):
        return -1
    else:
        sorted_chars = sorted(s)
        return ''.join(sorted_chars)

# Input
t = int(input())
queries = []
for _ in range(t):
    queries.append(input())

# Output
for query in queries:
    result = rearrange_string(query)
    print(result)
