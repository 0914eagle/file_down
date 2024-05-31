
def shortest_contiguous_subarray(N, K, M, array, queries):
    def check_subarray(subarray):
        return all(subarray.count(i) > 0 for i in range(1, K+1))

    def shortest_subarray_with_all_numbers():
        min_length = float('inf')
        for i in range(N):
            for j in range(i, N):
                subarray = array[i:j + 1]
                if check_subarray(subarray):
                    min_length = min(min_length, len(subarray))
        return min_length if min_length != float('inf') else -1

    output = []
    for query in queries:
        if query[0] == 1:
            array[query[1] - 1] = query[2]
        elif query[0] == 2:
            output.append(shortest_subarray_with_all_numbers())

    return output

# Input parsing
N, K, M = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

# Solve problem and print output
output = shortest_contiguous_subarray(N, K, M, array, queries)
for result in output:
    print(result)
