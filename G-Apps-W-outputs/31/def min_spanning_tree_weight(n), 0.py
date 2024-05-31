
def min_spanning_tree_weight(n):
    # Bitwise XOR of consecutive numbers from 0 to n-1 is always n
    return n

# Read input
n = int(input())

# Call the function and print the result
result = min_spanning_tree_weight(n)
print(result)
