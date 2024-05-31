
def schedule_exams(n, m, exams):
    schedule = [0] * n
    for i in range(m):
        s, d, c = exams[i]
        if d - s < c:
            return [-1]
        for j in range(s, d - 1):
            if schedule[j] != 0:
                return [-1]
            schedule[j] = i + 1
        schedule[d - 1] = m + 1
    return schedule

n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)
print(*result)
