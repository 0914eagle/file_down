
# Read the input
A, B, K = map(int, input().split())

# Print the output
for i in range(A, B + 1):
    if i <= K or i >= B - K + 1:
        print(i)

