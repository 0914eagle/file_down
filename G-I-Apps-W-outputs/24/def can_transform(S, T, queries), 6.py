
def can_transform(S, T, queries):
    def transform_string(string):
        stack = []
        for char in string:
            stack.append(char)
            while len(stack) >= 2 and stack[-2:] in [('A', 'B'), ('B', 'C'), ('C', 'A')]:
                stack.pop()
                stack.pop()
        return ''.join(stack)

    transformed_s = transform_string(S)
    transformed_t = transform_string(T)

    results = ''
    for query in queries:
        a, b, c, d = query
        if transformed_t in transformed_s[a-1:b]:
            results += '1'
        else:
            results += '0'

    return results

# Input parsing
S = input().strip()
T = input().strip()
num_queries = int(input())
queries = [list(map(int, input().split())) for _ in range(num_queries)]

# Call the function with the input data and print the result
print(can_transform(S, T, queries))
