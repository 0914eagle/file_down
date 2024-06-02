
def solve(N, H):
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i+1] += 1
    return "Yes" if H == sorted(H) else "No"

N = int(input())
H = list(map(int, input().split()))
print(solve(N, H))

