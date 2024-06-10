
def solve(q, queries):
    f = ["What are you doing at the end of the world? Are you busy? Will you save us?"]
    for n, k in queries:
        while len(f) <= n:
            f.append("What are you doing while sending " + f[-1] + "? Are you busy? Will you send " + f[-1] + "?")
        if len(f[n]) < k:
            return "."
        else:
            return f[n][k - 1]

q = int(input())
queries = []
for _ in range(q):
    n, k = map(int, input().split())
    queries.append((n, k))

print(solve(q, queries))

