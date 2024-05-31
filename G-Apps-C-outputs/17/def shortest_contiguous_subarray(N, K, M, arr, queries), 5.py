
def shortest_contiguous_subarray(N, K, M, arr, queries):
    def is_valid_subarray(subarray):
        return all(x in subarray for x in range(1, K+1))

    result = []
    for query in queries:
        if query[0] == 1:
            arr[query[1] - 1] = query[2]
        elif query[0] == 2:
            min_length = float('inf')
            for i in range(N):
                for j in range(i, N):
                    subarray = arr[i:j+1]
                    if is_valid_subarray(subarray):
                        min_length = min(min_length, len(subarray))
            if min_length == float('inf'):
                result.append(-1)
            else:
                result.append(min_length)

    return result

# Input processing
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))

queries = []
for _ in range(M):
    query = input().split()
    if query[0] == '1':
        queries.append((1, int(query[1]), int(query[2]))
    elif query[0] == '2':
        queries.append((2,))

output = shortest_contiguous_subarray(N, K, M, arr, queries)

for ans in output:
    print(ans)
