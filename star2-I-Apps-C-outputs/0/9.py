
def find_smallest_set(n, k, matches, disqualified):
    return 0

n, k = map(int, input().split())
matches = [list(map(int, input().split())) for _ in range(n)]
disqualified = list(map(int, input().split()))
print(find_smallest_set(n, k, matches, disqualified))

