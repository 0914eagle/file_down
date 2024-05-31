
def solve_time_machine_resistor(a, b):
    count = 0

    while a != 0:
        count += b // a
        b, a = a, b % a

    return count

# Read input
a, b = map(int, input().split())

# Solve the problem and print the output
print(solve_time_machine_resistor(a, b))
