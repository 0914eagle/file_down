
def divide_orange(n, k, a):
    segments = list(range(1, n*k+1))
    result = []
    
    for i in range(k):
        child_segments = segments[i*n:(i+1)*n]
        result.append(child_segments)
    
    for j in range(n):
        for i in range(k):
            print(result[i][j], end=' ')
    
divide_orange(2, 2, [4, 1])
# divide_orange(3, 1, [2])
