
def divide_orange(n, k, segments):
    result = []
    for i in range(n):
        child_segments = []
        for j in range(k):
            child_segments.append(segments[j] + i * k)
        result.append(child_segments)
    
    for child in result:
        print(' '.join(map(str, child)))

# Input reading
n, k = map(int, input().split())
segments = list(map(int, input().split()))

divide_orange(n, k, segments)
