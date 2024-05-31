
def divide_orange(n, k, segments):
    result = []
    current_segment = 1
    
    for i in range(n):
        child_segments = []
        for j in range(k):
            child_segments.append(current_segment)
            current_segment += 1
        result.append(child_segments)
    
    for i, segment in enumerate(segments):
        result[i].remove(segment)
        result[i].insert(0, segment)
    
    for child_segments in result:
        print(' '.join(map(str, child_segments)))

# Input parsing
n, k = map(int, input().split())
segments = list(map(int, input().split()))

divide_orange(n, k, segments)
