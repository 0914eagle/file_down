
def solve(K):
    return 2 * (K // 2) * ((K+1) // 2)

if __name__ == '__main__':
    K = int(input())
    print(solve(K))

