
N, D = map(int, input().split())

def minimum_number_of_inspectors(N, D):
    inspectors = [False] * N
    for i in range(N):
        start = max(0, i - D)
        end = min(N - 1, i + D)
        for j in range(start, end + 1):
            inspectors[j] = True
    
    return inspectors.count(True)

print(minimum_number_of_inspectors(N, D))

