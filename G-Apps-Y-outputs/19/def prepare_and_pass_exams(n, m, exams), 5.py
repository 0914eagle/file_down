
def prepare_and_pass_exams(n, m, exams):
    schedule = [0] * n
    
    for i, exam in enumerate(exams, start=1):
        s, d, c = exam
        
        # Check if Petya can prepare for the exam
        if d - s < c:
            return -1
        
        # Fill in the preparation days
        for j in range(s, d-1):
            if c > 0:
                schedule[j] = i
                c -= 1
        
        # Fill in the exam day
        schedule[d-1] = m + 1
    
    return schedule

# Read input
n, m = map(int, input().split())
exams = []
for _ in range(m):
    s, d, c = map(int, input().split())
    exams.append((s, d, c))

# Call the function and print the output
result = prepare_and_pass_exams(n, m, exams)
if result == -1:
    print(-1)
else:
    print(*result)
