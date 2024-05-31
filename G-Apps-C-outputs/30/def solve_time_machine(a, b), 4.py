
def solve_time_machine(a, b):
    # Recursive function to find the smallest number of resistors needed
    def find_resistors_needed(num, denom):
        if num == 1 and denom == 1:
            return 1
        elif num > denom:
            return num // denom + find_resistors_needed(num % denom, denom)
        else:
            return denom // num + find_resistors_needed(denom % num, num)

    return find_resistors_needed(a, b)

# Read input
a, b = map(int, input().split())

# Call the function and print the result
print(solve_time_machine(a, b))
