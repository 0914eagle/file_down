
def solve(s, queries):
    pass

n, q = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(q)]

print(*solve(s, queries), sep='\n')

