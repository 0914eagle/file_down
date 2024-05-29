
def check_dishes(t, test_cases):
    results = []
    
    for i in range(t):
        m, k = test_cases[i][0]
        a = test_cases[i][1]
        observations = test_cases[i][2:]
        
        taken = [0] * (k+1)
        still_available = [True] * (k+1)
        
        for j in range(m - 1):
            dish, disappointed = observations[j]
            if dish != 0:
                if not disappointed and still_available[dish]:
                    taken[dish] += 1
                still_available[dish] = False
            
        result = ""
        for j in range(1, k+1):
            if taken[j] + (a[j-1] - taken[j]) > m - 1:
                result += "Y"
            else:
                result += "N"
        
        results.append(result)
    
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    observations = [tuple(map(int, input().split())) for _ in range(m - 1)]
    test_cases.append((m, k, a, observations))

# Call the function and print the results
results = check_dishes(t, test_cases)
for result in results:
    print(result)
```
