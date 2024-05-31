
import bisect

class Student:
    def __init__(self, idx, a, b):
        self.idx = idx
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.a

def find_helper(students, new_student):
    idx = bisect.bisect_left(students, new_student)
    if idx == 0:
        return "NE"
    best_student = students[idx - 1]
    return str(best_student.idx)

def exam_village(N, queries):
    students = []
    results = []
    for i in range(N):
        query = queries[i].split()
        if query[0] == 'D':
            new_student = Student(i, int(query[1]), int(query[2]))
            students.append(new_student)
            students.sort()
        elif query[0] == 'P':
            result = find_helper(students, Student(int(query[1]), float('inf'), float('inf')))
            results.append(result)
    return results

# Input processing
N = int(input())
queries = []
for _ in range(N):
    queries.append(input())

# Call the function and output results
results = exam_village(N, queries)
for result in results:
    print(result)
