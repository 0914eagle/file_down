
import bisect

students = []
helped_by = []

def find_best_student(student):
    idx = bisect.bisect_left(students, student)
    if idx == 0:
        return "NE"
    return helped_by[idx-1]

def add_student(student):
    idx = bisect.bisect_left(students, student)
    students.insert(idx, student)
    helped_by.insert(idx, find_best_student(student))

N = int(input())
for _ in range(N):
    query = input().split()
    if query[0] == 'D':
        student = (int(query[1]), int(query[2]))
        add_student(student)
    elif query[0] == 'P':
        i = int(query[1])
        print(find_best_student(students[i-1]))

