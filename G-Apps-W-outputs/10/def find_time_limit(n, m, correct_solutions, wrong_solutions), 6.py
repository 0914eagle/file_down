
def find_time_limit(n, m, correct_solutions, wrong_solutions):
    max_correct = max(correct_solutions)
    min_wrong = min(wrong_solutions)
    
    if 2 * max_correct <= min_wrong:
        return max_correct
    else:
        return -1

# Input processing
n, m = map(int, input().split())
correct_solutions = list(map(int, input().split()))
wrong_solutions = list(map(int, input().split()))

# Call the function and print the result
result = find_time_limit(n, m, correct_solutions, wrong_solutions)
print(result)
