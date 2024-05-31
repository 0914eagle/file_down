
def shortest_subarray_length(N, K, M, arr, queries):
    def is_valid_subarray(subarray):
        return len(set(subarray)) == K

    def shortest_subarray(arr):
        min_length = float('inf')
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray = arr[i:j+1]
                if is_valid_subarray(subarray):
                    min_length = min(min_length, len(subarray))
        return min_length if min_length != float('inf') else -1

    result = []
    for query in queries:
        if query[0] == 1:
            arr[query[1]-1] = query[2]
        elif query[0] == 2:
            result.append(shortest_subarray(arr))

    return result

# Input processing
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

output = shortest_subarray_length(N, K, M, arr, queries)
for ans in output:
    print(ans)
