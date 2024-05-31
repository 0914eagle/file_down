
def schedule_exams(n, m, exams):
    schedule = [0] * n
    
    exam_days = []
    for i in range(m):
        exam_days.append((exams[i][0], exams[i][1], exams[i][2], i+1))
    
    exam_days.sort()
    
    for exam in exam_days:
        start_day, end_day, prep_days, exam_num = exam
        for i in range(start_day, end_day):
            if prep_days == 0:
                schedule[i-1] = exam_num
            else:
                if schedule[i-1] == 0:
                    schedule[i-1] = exam_num
                    prep_days -= 1
                else:
                    break
        if prep_days != 0:
            print(-1)
            return
        
    for i in range(n):
        if schedule[i] == 0:
            schedule[i] = m + 1
    
    print(*schedule)

n, m = map(int, input().split())
exams = []
for _ in range(m):
    s, d, c = map(int, input().split())
    exams.append((s, d, c))

schedule_exams(n, m, exams)
