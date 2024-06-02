
def solve_problem(numbers):
    # Extract the values from the input
    a1, a2, a3, a4, a5 = numbers

    # Perform the required calculations
    result = (a1 * a2) // (a3 + a4 + a5)

    return result

# Read input from the user
input_numbers = list(map(int, input().split()))

# Call the function with the input and print the result
print(solve_problem(input_numbers))
