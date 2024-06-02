
import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    S = input().rstrip()
    A = [0] * (N + 1)
    C = [0] * (N + 1)
    G = [0] * (N + 1)
    T = [0] * (N + 1)
    for i in range(N):
        if S[i] == "A":
            A[i + 1] = A[i] + 1
        elif S[i] == "C":
            C[i + 1] = C[i] + 1
        elif S[i] == "G":
            G[i + 1] = G[i] + 1
        else:
            T[i + 1] = T[i] + 1
    for i in range(Q):
        l, r = map(int, input().split())
        print(C[r] - C[l - 1] - (A[r] - A[l - 1]))

if __name__ == "__main__":
    main()

