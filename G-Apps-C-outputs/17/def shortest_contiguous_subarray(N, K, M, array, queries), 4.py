
def shortest_contiguous_subarray(N, K, M, array, queries):
    result = []
    
    def find_shortest_subarray():
        counts = [0] * K
        missing = K
        left = 0
        min_length = float('inf')
        for right in range(N):
            if counts[array[right] - 1] == 0:
                missing -= 1
            counts[array[right] - 1] += 1
            
            while missing == 0:
                min_length = min(min_length, right - left + 1)
                counts[array[left] - 1] -= 1
                if counts[array[left] - 1] == 0:
                    missing += 1
                left += 1
        return min_length if min_length != float('inf') else -1
    
    for query in queries:
        if query[0] == 1:
            array[query[1] - 1] = query[2]
        else:
            result.append(find_shortest_subarray())
    
    return result

# Input
N, K, M = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(M):
    query = list(map(int, input().split()))
    queries.append(query)

# Output
output = shortest_contiguous_subarray(N, K, M, array, queries)
for res in output:
    print(res)
