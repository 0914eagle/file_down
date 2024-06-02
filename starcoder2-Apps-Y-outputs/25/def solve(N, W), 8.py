
def solve(N, W):
    words = set()
    for w in W:
        if w in words:
            return 'No'
        if len(words) > 0 and w[0] != W[-1][-1]:
            return 'No'
        words.add(w)
    return 'Yes'

N = int(input())
W = [input() for _ in range(N)]
print(solve(N, W))

