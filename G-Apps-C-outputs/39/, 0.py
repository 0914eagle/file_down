
import heapq

class Student:
    def __init__(self, index, a, b):
        self.index = index
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.a

def find_help(query_list):
    result = []
    students = []
    for query in query_list:
        if query[0] == 'D':
            a, b = int(query[1]), int(query[2])
            student = Student(len(students), a, b)
            heapq.heappush(students, student)
        else:
            a, b = int(query[1]), int(query[2])
            found = False
            while students:
                current_student = heapq.heappop(students)
                if current_student.a >= a and current_student.b >= b:
                    result.append(current_student.index + 1)
                    found = True
                    break
            if not found:
                result.append('NE')
    return result

# Reading input
n = int(input())
queries = [input().split() for _ in range(n)]

# Calling the function and printing the output
output = find_help(queries)
for o in output:
    print(o)
