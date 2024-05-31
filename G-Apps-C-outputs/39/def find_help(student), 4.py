
import bisect

students = []

def find_help(student):
    idx = bisect.bisect_left(students, student)
    if idx == 0:
        return "NE"
    else:
        prev_student = students[idx - 1]
        if prev_student[0] >= student[0] and prev_student[1] >= student[1]:
            return students.index(prev_student) + 1
        else:
            return "NE"

def process_query(query):
    if query[0] == "D":
        student = (query[1], query[2])
        students.append(student)
        students.sort()
    elif query[0] == "P":
        student_idx = query[1] - 1
        if student_idx >= len(students):
            print("NE")
        else:
            print(find_help(students[student_idx]))

N = int(input())
for _ in range(N):
    query = input().split()
    if len(query) == 3:
        query[1] = int(query[1])
        query[2] = int(query[2])
    else:
        query[1] = int(query[1]) 
    process_query(query)
