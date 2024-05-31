
def schedule_exams(n, m, exams):
    schedule = [0] * n
    exam_days = sorted([(exam[0], i) for i, exam in enumerate(exams)])
    
    for day in range(n):
        available_exams = [i for s, d, c, i in exams if s <= day < d and schedule[day] == 0]
        if len(available_exams) == 1:
            exam_idx = available_exams[0]
            schedule[day] = exam_idx + 1
            for prep_day in range(day - exams[exam_idx][2] + 1, day):
                if schedule[prep_day] == 0:
                    schedule[prep_day] = exam_idx + 1
        elif len(available_exams) > 1:
            return [-1]
    
    return schedule

n, m = map(int, input().split())
exams = [list(map(int, input().split())) + [i] for i in range(m)]

output = schedule_exams(n, m, exams)
if output[0] == -1:
    print(-1)
else:
    print(' '.join(map(str, output)))
