
def max_visitors(t, test_cases):
    visitors = []
    
    for i in range(t):
        a, b, c = test_cases[i]
        
        if a == 0 and b == 0 and c == 0:
            visitors.append(0)
        elif a == 0 or b == 0 or c == 0:
            visitors.append(1)
        else:
            min_val = min(a, b, c)
            max_val = max(a, b, c)
            sum_val = a + b + c
            
            if min_val == 1:
                visitors.append(min(sum_val, 2))
            else:
                visitors.append(min_val + min(max_val - min_val, 1) + min(min_val, 1))
    
    return visitors

# Input
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Output
results = max_visitors(t, test_cases)
for res in results:
    print(res)
