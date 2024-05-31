
import bisect

def find_student_to_ask(queries):
    students = []
    results = []

    for query in queries:
        if query[0] == 'D':
            a, b = query[1], query[2]
            bisect.insort(students, (a, b))

        if query[0] == 'P':
            idx = bisect.bisect_left(students, (query[1], float('inf')))
            if idx == len(students):
                results.append("NE")
            else:
                results.append(students[idx][1])

    return results

# Input processing
N = int(input())
queries = []
for _ in range(N):
    query = input().split()
    if query[0] == 'D':
        queries.append((query[0], int(query[1]), int(query[2]))
    elif query[0] == 'P':
        queries.append((query[0], int(query[1])))

# Call the function and output the results
results = find_student_to_ask(queries)
for result in results:
    print(result)
