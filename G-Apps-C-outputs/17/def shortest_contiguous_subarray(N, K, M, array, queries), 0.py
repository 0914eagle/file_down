
def shortest_contiguous_subarray(N, K, M, array, queries):
    def check_subarray(subarray):
        return len(set(subarray)) == K

    result = []
    for query in queries:
        if query[0] == 1:
            array[query[1] - 1] = query[2]
        elif query[0] == 2:
            min_length = float('inf')
            for i in range(N):
                for j in range(i, N):
                    if check_subarray(array[i:j+1]):
                        min_length = min(min_length, j - i + 1)
            result.append(min_length if min_length != float('inf') else -1)

    return result

# Input parsing
N, K, M = map(int, input().split())
array = list(map(int, input().split()))

queries = []
for _ in range(M):
    query = input().split()
    if query[0] == '1':
        queries.append((1, int(query[1]), int(query[2]))
    elif query[0] == '2':
        queries.append((2,))

output = shortest_contiguous_subarray(N, K, M, array, queries)

for res in output:
    print(res)
