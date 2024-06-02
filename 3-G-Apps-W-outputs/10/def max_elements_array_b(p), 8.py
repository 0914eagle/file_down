
def max_elements_array_b(p):
    n = len(p)
    count = 1
    while n > 1:
        if p[-1] == '0':
            p = p[:-1]
            n -= 1
        else:
            count += 1
            p = p[:-1]
            n -= 1
    return count

# Read input
p = input().strip()

# Call the function and print the result
print(max_elements_array_b(p))
