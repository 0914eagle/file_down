
def divide_orange(n, k, children_segments):
    result = []
    orange_segments = list(range(1, n*k + 1))
    
    for i in range(k):
        child_segment = [children_segments[i]]
        remaining_segments = orange_segments.copy()
        remaining_segments.remove(children_segments[i])
        
        for j in range(n-1):
            child_segment.append(remaining_segments.pop(0))
        
        result.append(child_segment)
    
    for child_segments in result:
        print(' '.join(map(str, child_segments)))

# Input parsing
n, k = map(int, input().split())
children_segments = list(map(int, input().split()))

# Call the function with input values
divide_orange(n, k, children_segments)
