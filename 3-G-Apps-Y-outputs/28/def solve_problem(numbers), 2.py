
def solve_problem(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

input_numbers = list(map(int, input().split()))
output_result = solve_problem(input_numbers)
print(output_result)
