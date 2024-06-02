
def solve(r, n, booked):
    for i in range(1, r + 1):
        if i not in booked:
            return i
    return "too late"

r, n = map(int, input().split())
booked = [int(input()) for _ in range(n)]
print(solve(r, n, booked))

