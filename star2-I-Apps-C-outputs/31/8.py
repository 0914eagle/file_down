
def solve(n, m, words):
    pass

n, m = map(int, input().split())
words = []
for _ in range(n):
    l, *s = map(int, input().split())
    words.append((l, s))

result = solve(n, m, words)
if result is None:
    print("No")
else:
    print("Yes")
    print(len(result))
    print(" ".join(map(str, result)))

