
def schedule_exams(n, m, exams):
    schedule = [0] * n
    for i in range(m):
        start_day, exam_day, prepare_days = exams[i]
        if exam_day - start_day <= prepare_days:
            return [-1] 
        for j in range(start_day, exam_day - 1):
            if schedule[j] == 0:
                schedule[j] = i + 1
            else:
                return [-1]
    return schedule

n, m = map(int, input().split())
exams = []
for _ in range(m):
    s, d, c = map(int, input().split())
    exams.append((s, d, c))

result = schedule_exams(n, m, exams)
print(" ".join(map(str, result)))
