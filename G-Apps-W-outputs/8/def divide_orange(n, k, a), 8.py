
def divide_orange(n, k, a):
    segments = [i for i in range(1, n*k+1)]
    children_segments = [[] for _ in range(k)]
    
    for i, num in enumerate(a):
        children_segments[i].append(num)
    
    curr_child = 0
    for i in range(n):
        for _ in range(k):
            children_segments[curr_child].append(segments.pop(0))
            curr_child = (curr_child + 1) % k
    
    for child_segments in children_segments:
        print(" ".join(map(str, child_segments)))

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

divide_orange(n, k, a)
