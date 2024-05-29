
def calculate_minimal_marks_to_add(n, k, marks):
    current_total_marks = sum(marks)
    current_average = current_total_marks / n
    target_average = k
    
    if current_average >= target_average:
        return 0
    
    total_possible_marks = n
    while True:
        total_marks_required = total_possible_marks * target_average - current_total_marks
        remaining_marks = total_marks_required % total_possible_marks
        if remaining_marks == 0:
            return total_marks_required // total_possible_marks
        total_possible_marks += 1

# Input parsing
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Calculate and print minimal number of marks to add
print(calculate_minimal_marks_to_add(n, k, marks))
```
