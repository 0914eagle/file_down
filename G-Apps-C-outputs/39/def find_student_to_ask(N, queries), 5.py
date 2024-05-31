
import heapq

def find_student_to_ask(N, queries):
    students = []
    for i in range(N):
        query = queries[i]
        if query[0] == 'D':
            heapq.heappush(students, (query[1], query[2], i+1))
        else:
            student = query[1]
            found = False
            while students:
                a, b, idx = heapq.heappop(students)
                if a >= student[0] and b >= student[1]:
                    print(idx)
                    found = True
                    break
            if not found:
                print("NE")

# Input parsing
N = int(input())
queries = []
for _ in range(N):
    query = input().split()
    if query[0] == 'D':
        queries.append(('D', int(query[1]), int(query[2])))
    else:
        queries.append(('P', int(query[1])))

find_student_to_ask(N, queries)
