
def divide_orange(n, k, a):
    orange_segments = list(range(1, n*k + 1))
    result = []
    
    for i in range(k):
        child_segments = list(range(i*n + 1, (i+1)*n + 1))
        result.append(child_segments)
        orange_segments = [seg for seg in orange_segments if seg not in child_segments]
    
    for i in range(n-k):
        for j in range(k):
            result[j].append(orange_segments.pop())
    
    for child_segments in result:
        print(' '.join(map(str, child_segments)))
    
# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

divide_orange(n, k, a)
