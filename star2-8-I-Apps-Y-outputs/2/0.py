
def solve(N, A):
    A = sorted(A)
    x = A[N//2]
    ans = 0
    for a in A:
        ans += abs(a - x)
    
    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


if __name__ == '__main__':
    main()

