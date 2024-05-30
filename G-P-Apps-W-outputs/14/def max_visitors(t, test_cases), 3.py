
# Function to solve the problem
def max_visitors(t, test_cases):
    for i in range(t):
        a, b, c = test_cases[i]
        # Calculate the maximum number of visitors Denis can feed
        # by distributing the dishes in a smart way
        max_visitors = min(a, b, c) + (a + b + c - min(a, b, c)) // 2
        print(max_visitors)

# Input processing
t = int(input()) # Number of test cases
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Call the function with input parameters
max_visitors(t, test_cases)
```
