
def remaining_number(T, queries):
    results = []
    
    for n, x in queries:
        result = x*2
        results.append(result)
    
    return results

T = 3
queries = [(3, 1), (4, 2), (69, 6)]
output = remaining_number(T, queries)

for num in output:
    print(num)
