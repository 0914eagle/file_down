
def solve(N, A):
    A.sort()
    return sum(A[1::2])

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

