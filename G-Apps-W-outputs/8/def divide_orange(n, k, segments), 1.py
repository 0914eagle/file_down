
def divide_orange(n, k, segments):
    result = []
    curr_segment = 1
    for i in range(k):
        current_child = [segments[i]]
        for j in range(n-1):
            current_child.append(curr_segment)
            curr_segment += 1
        result.append(current_child)
    
    for i in range(n):
        for j in range(k):
            print(result[j][i], end=' ')
        print()

# Input parsing
n, k = map(int, input().split())
segments = list(map(int, input().split()))

divide_orange(n, k, segments)
