
def solve_problem(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Input
input_numbers = list(map(int, input().split()))

# Output
print(solve_problem(input_numbers))
