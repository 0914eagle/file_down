
def find_student_helper(queries):
    students = []
    results = []
    
    for query in queries:
        if query[0] == 'D':
            a, b = map(int, query[1:])
            students.append((a, b))
        elif query[0] == 'P':
            i = int(query[1])
            min_diff = float('inf')
            min_diff_student = None
            
            for j, (a, b) in enumerate(students):
                if a >= students[i-1][0] and b >= students[i-1][1]:
                    diff = abs(a - students[i-1][0]) + abs(b - students[i-1][1])
                    if diff < min_diff or (diff == min_diff and a < min_diff_student[0]):
                        min_diff = diff
                        min_diff_student = (a, j)
            
            if min_diff_student:
                results.append(str(min_diff_student[1] + 1))
            else:
                results.append("NE")
    
    return results

# Input
N = int(input())
queries = [input().split() for _ in range(N)]

# Output
for res in find_student_helper(queries):
    print(res)
