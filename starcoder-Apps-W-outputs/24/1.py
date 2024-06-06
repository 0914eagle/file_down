
def read_matrix(n, m):
    return [list(map(int, input().split())) for _ in range(n)]

def get_max(items):
    return max(items)

def get_min(items):
    return min(items)

def get_sum(items):
    return sum(items)

def get_median(items):
    items.sort()
    return items[len(items)//2]

def input_matrix(n, m):
    return [list(map(int, input().split())) for _ in range(n)]

n = int(input())
items = sorted(list(map(int, input().split())))

if len(items) < 2 * n:
    print("impossible")
    exit(0)

max_item = get_max(items)
min_item = get_min(items)

if max_item - min_item > 2 ** 28:
    print("impossible")
    exit(0)

s = get_sum(items) - max_item

if (s & 1) or s < 2 * min_item:
    print("impossible")
    exit(0)

min_item = (s - max_item) // 2
max_item = s - min_item

r = []
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i] + items[j] == min_item:
            r.append((i, j))

ans = [0] * n
for i in range(n):
    for j in range(i):
        ans[i] += (items[j] == max_item)
        ans[j] += (items[i] == max_item)

for a, b in r:
    ans[a] += (items[b] == max_item)
    ans[b] += (items[a] == max_item)

print(*ans)
