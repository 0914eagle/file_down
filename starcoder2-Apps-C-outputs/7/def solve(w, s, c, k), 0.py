
def solve(w, s, c, k):
    if w == 0 and s == 0 and c == 0:
        return True
    if w > 0 and s > 0 and c > 0:
        return False
    if w > 0 and s > 0:
        return False
    if w > 0 and c > 0:
        return False
    if s > 0 and c > 0:
        return False
    if w > k or s > k or c > k:
        return False
    if w > 0:
        return solve(w - 1, s, c, k) or solve(w, s - 1, c, k) or solve(w, s, c - 1, k)
    if s > 0:
        return solve(w, s - 1, c, k) or solve(w, s, c - 1, k)
    if c > 0:
        return solve(w, s, c - 1, k)

w, s, c, k = map(int, input().split())
if solve(w, s, c, k):
    print("YES")
else:
    print("NO")
