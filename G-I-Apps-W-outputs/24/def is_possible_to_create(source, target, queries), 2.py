
def is_possible_to_create(source, target, queries):
    def is_possible(source, target):
        if len(source) < len(target):
            return False
        if len(target) == 0:
            return True
        
        if source == target:
            return True
        
        if 'AAA' in source:
            source = source.replace('AAA', '')
        
        if source != target:
            return is_possible(source.replace('A', 'BC').replace('B', 'AC').replace('C', 'AB'), target)
        
        return True

    results = ''
    for query in queries:
        a, b, c, d = query
        if is_possible(source[a-1:b], target[c-1:d]):
            results += '1'
        else:
            results += '0'
    
    return results

# Input parsing
S = input().strip()
T = input().strip()
Q = int(input().strip())

queries = []
for _ in range(Q):
    a, b, c, d = map(int, input().strip().split())
    queries.append((a, b, c, d))

# Call the function with input and print the result
print(is_possible_to_create(S, T, queries))
