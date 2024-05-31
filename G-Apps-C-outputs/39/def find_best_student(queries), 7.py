
import heapq

def find_best_student(queries):
    students = []
    
    for query in queries:
        if query[0] == 'D':
            heapq.heappush(students, (query[2], query[1], len(students) + 1))
        elif query[0] == 'P':
            a_i, b_i = query[1], float('inf')
            
            while students:
                b, a, i = heapq.heappop(students)
                if a >= a_i and b >= b_i:
                    return i
                b_i = b
            
            print('NE')
    return

# Read input
N = int(input())
queries = []
for _ in range(N):
    query = input().split()
    if query[0] == 'D':
        queries.append(('D', int(query[1]), int(query[2])))
    elif query[0] == 'P':
        queries.append(('P', int(query[1])))

# Solve problem
find_best_student(queries)
