
def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize schedule with rest days
    
    # Sort the exams by the day questions are given
    exams.sort(key=lambda x: x[0])
    
    for i, exam in enumerate(exams):
        s, d, c = exam
        prepare_day = None
        
        for day in range(s, d):
            if days[day - 1] == 0:  # Check if the day is available for preparation
                if prepare_day is None or day - prepare_day >= c:
                    days[day - 1] = i + 1
                    prepare_day = day
        
        if prepare_day is None:  # If no suitable preparation day found
            return -1
    
    return days

# Input
n, m = map(int, input().split())
exams = [list(map(int, input().split())) for _ in range(m)]

# Output
result = schedule_exams(n, m, exams)
if result == -1:
    print(-1)
else:
    print(*result)
