

def solve(A, B, k1, k2):
    n = len(A)
    A.sort()
    B.sort()
    if k1 + k2 >= n:
        return 0
    
    diff = [A[i] - B[i] for i in range(n)]
    diff.sort(key=abs)
    
    for i in range(k1 + k2):
        diff[i] = abs(diff[i])
    
    return sum(x*x for x in diff)
    
n, k1, k2 = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solve(A, B, k1, k2))


