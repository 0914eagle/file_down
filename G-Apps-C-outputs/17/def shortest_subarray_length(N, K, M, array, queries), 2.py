
def shortest_subarray_length(N, K, M, array, queries):
    positions = {i: -1 for i in range(1, K+1)}
    min_length = float('inf')
    nums_missing = K
    
    def update_min_length(pos):
        nonlocal min_length
        start = min(positions.values())
        min_length = min(min_length, pos - start + 1)
    
    for i, num in enumerate(array):
        if num in positions and positions[num] == -1:
            positions[num] = i
            nums_missing -= 1
        if nums_missing == 0:
            update_min_length(i)
    
    result = []
    for query in queries:
        if query[0] == 1:
            p, v = query[1], query[2]
            p -= 1
            old_value = array[p]
            if positions[old_value] == p:
                positions[old_value] = -1
                nums_missing += 1
            array[p] = v
            if v in positions and positions[v] == -1:
                positions[v] = p
                nums_missing -= 1
            if nums_missing == 0:
                update_min_length(p)
        elif query[0] == 2:
            result.append(min_length if min_length != float('inf') else -1)
    
    return result

# Input parsing
N, K, M = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

# Call the function with input values
output = shortest_subarray_length(N, K, M, array, queries)

# Print the output
for length in output:
    print(length)
