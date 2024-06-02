
def solve(N, H):
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            return "No"
    return "Yes"

N = int(input())
H = list(map(int, input().split()))
print(solve(N, H))

