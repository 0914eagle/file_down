
def solve(n, s, data):
    data.sort(key=lambda x: x[1])
    time = 0
    for f, t in data:
        time += abs(f - s)
        time += t
        s = f
    
    return time
n, s = map(int, input().split())
data = []
for _ in range(n):
    f, t = map(int, input().split())
    data.append((f, t))
print(solve(n, s, data))

