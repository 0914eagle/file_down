
def solve(s, k):
    num_count = [0] * 10
    for c in s:
        num_count[int(c)] += 1
    for i in range(1, 10):
        num_count[i] += num_count[i - 1]
    for i in range(1, 10):
        num_count[i] += num_count[i - 1] * (10 ** (i - 1))
    for i in range(1, 10):
        num_count[i] += num_count[i - 1] * (5 * 10 ** 15)
    for i in range(1, 10):
        if num_count[i] >= k:
            return str(i)
    return ""

s = input()
k = int(input())
print(solve(s, k))

