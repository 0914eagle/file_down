
def schedule_exams(n, m, exams):
    schedule = [0] * n
    for i, (s, d, c) in enumerate(exams, start=1):
        if d - s < c:
            return [-1]
        for day in range(s, d - c):
            if schedule[day] != 0:
                return [-1]
            schedule[day] = i
        schedule[d - c] = m + 1
    return schedule

n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)
print(*result)
