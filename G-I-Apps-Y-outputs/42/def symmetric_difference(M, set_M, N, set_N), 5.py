
def symmetric_difference(M, set_M, N, set_N):
    diff_M = set_M.difference(set_N)
    diff_N = set_N.difference(set_M)
    symmetric_diff = sorted(diff_M.union(diff_N))
    for num in symmetric_diff:
        print(num)

if __name__ == "__main__":
    M = int(input())
    set_M = set(map(int, input().split()))
    N = int(input())
    set_N = set(map(int, input().split()))
    
    symmetric_difference(M, set_M, N, set_N)
