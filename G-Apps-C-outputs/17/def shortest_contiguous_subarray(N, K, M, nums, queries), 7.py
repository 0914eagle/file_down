
def shortest_contiguous_subarray(N, K, M, nums, queries):
    def is_valid_subarray(subarray):
        return len(set(subarray)) == K
    
    def shortest_subarray_with_all_nums():
        min_length = float('inf')
        for i in range(N):
            for j in range(i, N):
                subarray = nums[i:j+1]
                if is_valid_subarray(subarray):
                    min_length = min(min_length, len(subarray))
        return min_length if min_length != float('inf') else -1
    
    result = []
    for query in queries:
        if query[0] == 1:
            nums[query[1]-1] = query[2]
        elif query[0] == 2:
            result.append(shortest_subarray_with_all_nums())
    return result

N, K, M = map(int, input().split())
nums = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = input().split()
    if query[0] == '1':
        queries.append((1, int(query[1]), int(query[2])))
    elif query[0] == '2':
        queries.append((2,))

output = shortest_contiguous_subarray(N, K, M, nums, queries)
for res in output:
    print(res)
