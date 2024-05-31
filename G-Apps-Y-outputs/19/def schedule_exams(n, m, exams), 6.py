
def schedule_exams(n, m, exams):
    preparation = {}
    schedule = [0] * n

    for i, exam in enumerate(exams, start=1):
        s, d, c = exam
        prep_days = 0
        for j in range(s, d):
            if schedule[j - 1] != 0:  # If the day is already occupied
                break
            schedule[j - 1] = i
            prep_days += 1
            if prep_days == c:
                break
        if prep_days < c:
            return [-1]

    return schedule

n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]

result = schedule_exams(n, m, exams)
print(*result)
