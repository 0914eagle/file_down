
def validate_time_limit(n, m, correct_solutions, wrong_solutions):
    min_correct = min(correct_solutions)
    max_correct = max(correct_solutions)
    
    min_wrong = min(wrong_solutions)
    
    if 2 * min_correct <= max_correct and min_correct < min_wrong:
        return max_correct
    else:
        return -1

# Read input
n, m = map(int, input().split())
correct_solutions = list(map(int, input().split()))
wrong_solutions = list(map(int, input().split()))

# Output the result
print(validate_time_limit(n, m, correct_solutions, wrong_solutions))
