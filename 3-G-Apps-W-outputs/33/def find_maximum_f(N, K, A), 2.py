
def find_maximum_f(N, K, A):
    max_f = 0
    for i in range(41, -1, -1):  # Iterate through each bit position from 41 to 0
        count = 0
        mask = 1 << i
        new_max_f = max_f | (1 << i)  # Set the bit at position i in the new max_f
        for a in A:
            if a & mask:  # Check if the bit at position i is set in A
                count += 1
        if count <= N // 2:  # If the bit is set in less than half of the numbers
            max_f = new_max_f  # Update max_f
    return max_f

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find and print the maximum value of f
print(find_maximum_f(N, K, A))
