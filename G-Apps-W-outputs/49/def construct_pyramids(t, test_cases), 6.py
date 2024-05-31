
def construct_pyramids(t, test_cases):
    def num_pyramids(n):
        h = 1
        pyramids = 0
        while n >= h * (h+1) // 2:
            n -= h * (h+1) // 2
            pyramids += 1
            h += 1
        return pyramids
    
    results = []
    for n in test_cases:
        results.append(num_pyramids(n))
    
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(int(input()))

# Get results
results = construct_pyramids(t, test_cases)

# Output results
for r in results:
    print(r)
