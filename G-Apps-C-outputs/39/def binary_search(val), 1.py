
import bisect

students = []
sorted_students = []

def binary_search(val):
    left = 0
    right = len(sorted_students) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_students[mid][0] >= val:
            right = mid - 1
        else:
            left = mid + 1
    return left

def find_student_to_ask(A, B):
    index = binary_search((A, B))
    if index == len(sorted_students):
        return "NE"
    return sorted_students[index][2]

N = int(input())
for _ in range(N):
    query = input().split()
    if query[0] == 'D':
        A, B = map(int, query[1:])
        students.append((A, B, len(students) + 1))
        bisect.insort(sorted_students, (A, B, len(students)))

    elif query[0] == 'P':
        i = int(query[1])
        print(find_student_to_ask(students[i-1][0], students[i-1][1]))

[/PYTHON