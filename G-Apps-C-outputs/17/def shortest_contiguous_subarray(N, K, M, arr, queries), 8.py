
def shortest_contiguous_subarray(N, K, M, arr, queries):
    def check_subarray(sub_arr):
        return all(x in sub_arr for x in range(1, K + 1))

    def shortest_subarray(arr):
        min_len = float('inf')
        for i in range(N):
            for j in range(i, N):
                sub_arr = arr[i:j+1]
                if check_subarray(sub_arr):
                    min_len = min(min_len, len(sub_arr))
        return min_len if min_len != float('inf') else -1

    result = []
    for query in queries:
        if query[0] == 1:
            arr[query[1] - 1] = query[2]
        elif query[0] == 2:
            result.append(shortest_subarray(arr))

    return result

# Input parsing
N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = input().split()
    if query[0] == '1':
        p, v = map(int, query[1:])
        queries.append((1, p, v))
    elif query[0] == '2':
        queries.append((2,))

output = shortest_contiguous_subarray(N, K, M, arr, queries)
for res in output:
    print(res)
