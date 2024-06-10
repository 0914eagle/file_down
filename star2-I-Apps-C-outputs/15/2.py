
def solve(n, k):
    if n == 0:
        return "What are you doing at the end of the world? Are you busy? Will you save us?"
    else:
        return "What are you doing while sending " + solve(n - 1, k) + "? Are you busy? Will you send " + solve(n - 1, k) + "?"

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    print(solve(n, k)[k - 1] if k <= len(solve(n, k)) else '.')

