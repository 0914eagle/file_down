
import itertools

def redistribute_exams(n, students):
    room_order = list(range(1, n + 1))
    permutations = itertools.permutations(room_order)  # Generate all possible permutations of room orders
    
    for permutation in permutations:
        exams_pile = sum(students)
        students_in_room = students.copy()
        
        for room in permutation:
            exams_pile -= students_in_room[room - 1]
            if exams_pile < 0:
                break
            exams_pile += students_in_room[room - 1]
        
        if exams_pile >= 0:
            return permutation
        
    return "impossible"

# Input reading
n = int(input())
students = list(map(int, input().split()))

# Output
result = redistribute_exams(n, students)
if result == "impossible":
    print("impossible")
else:
    print(*result)
