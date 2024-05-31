
def shortest_contiguous_subarray(N, K, M, arr, queries):
    def is_valid_subarray(subarr):
        return all(i in subarr for i in range(1, K+1))

    def shortest_subarray(arr):
        min_len = float('inf')
        for i in range(N):
            for j in range(i, N):
                if is_valid_subarray(arr[i:j+1]):
                    min_len = min(min_len, j-i+1)
        return min_len if min_len != float('inf') else -1

    result = []
    for q in queries:
        if q[0] == 1:
            arr[q[1]-1] = q[2]
        elif q[0] == 2:
            result.append(shortest_subarray(arr))
    
    return result

# Input parsing
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

# Call the function and print the results
results = shortest_contiguous_subarray(N, K, M, arr, queries)
for res in results:
    print(res)
