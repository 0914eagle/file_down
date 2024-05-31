
def prepare_and_pass_exams(n, m, exams):
    schedule = [0] * n  # Initialize the schedule with resting days
    
    for i, exam in enumerate(exams):
        s, d, c = exam
        if d - s < c:  # Impossible to prepare for the exam
            return [-1]
        
        for j in range(s, d - 1):
            if schedule[j] != 0:  # Conflict in schedule
                return [-1]
            schedule[j] = i + 1
        schedule[d - 1] = m + 1  # Mark the day of the exam
    
    return schedule

# Input
n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = prepare_and_pass_exams(n, m, exams)

# Output
for day in result:
    print(day, end=' ')
