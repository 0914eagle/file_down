
n, c = map(int, input().split())
weights = list(map(int, input().split()))
def solution(n, c, weights):
    s = 0
    count = 0
    for i in range(n):
        if s + weights[i] <= c:
            s += weights[i]
            count += 1
    
    return count
print(solution(n, c, weights))

