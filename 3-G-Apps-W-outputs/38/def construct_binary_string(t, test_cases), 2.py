
def construct_binary_string(t, test_cases):
    results = []
    
    for i in range(t):
        n, s = test_cases[i]
        result = ""
        
        for j in range(n):
            result += s[j]
        
        results.append(result)
    
    return results

# Input parsing
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Call the function and print the results
results = construct_binary_string(t, test_cases)
for result in results:
    print(result)
