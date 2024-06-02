
def solve(r, n, booked):
    for i in range(1, r + 1):
        if i not in booked:
            return i
    return "too late"

r, n = map(int, input().split())
booked = set()
for _ in range(n):
    booked.add(int(input()))

print(solve(r, n, booked))

