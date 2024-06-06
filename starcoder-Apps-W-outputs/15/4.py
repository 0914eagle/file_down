
N = int(input())
all_intervals = []
for _ in range(N):
    s = input()
    if s[0] == '1':
        a, b = map(int, s[2:].split())
        all_intervals.append((a, b))
    elif s[0] == '2':
        a, b = map(int, s[2:].split())
        if a > b:
            a, b = b, a
        all_intervals = sorted(all_intervals)
        ans = 'NO'
        for i in range(len(all_intervals)):
            if i == 0 or all_intervals[i][0] >= all_intervals[i - 1][1]:
                if a <= all_intervals[i][0] <= b or a <= all_intervals[i][1] <= b:
                    ans = 'YES'
                    break
        print(ans)
