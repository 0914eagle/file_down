
def find_min_changes(s, k):
    n = len(s)
    count = [0] * 3
    for c in s:
        if c == 'R':
            count[0] += 1
        elif c == 'G':
            count[1] += 1
        else:
            count[2] += 1
    min_changes = n
    for i in range(n - k + 1):
        window_count = [0] * 3
        for j in range(i, i + k):
            if s[j] == 'R':
                window_count[0] += 1
            elif s[j] == 'G':
                window_count[1] += 1
            else:
                window_count[2] += 1
        changes = 0
        for j in range(3):
            changes += abs(count[j] - window_count[j])
        min_changes = min(min_changes, changes)
    return min_changes


q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    print(find_min_changes(s, k))

