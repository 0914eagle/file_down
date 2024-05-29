
def contest_start_time(current_time, hours_until_start):
    start_time = (current_time + hours_until_start) % 24
    return start_time

# Read input from standard input
A, B = map(int, input().split())

# Calculate and print the starting time of the contest
print(contest_start_time(A, B))
