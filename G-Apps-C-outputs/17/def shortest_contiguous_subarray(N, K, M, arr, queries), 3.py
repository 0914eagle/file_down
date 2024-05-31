
def shortest_contiguous_subarray(N, K, M, arr, queries):
    def is_valid_subarray(subarray, K):
        return len(set(subarray)) == K

    result = []
    for query in queries:
        if query[0] == 1:
            arr[query[1] - 1] = query[2]
        else:
            min_length = float('inf')
            for i in range(N):
                for j in range(i, N):
                    subarray = arr[i:j+1]
                    if is_valid_subarray(subarray, K):
                        min_length = min(min_length, len(subarray))
            result.append(min_length if min_length != float('inf') else -1)
    
    return result

# Read input
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

# Process queries
output = shortest_contiguous_subarray(N, K, M, arr, queries)

# Print output
for val in output:
    print(val)
