
def find_minimum_tl(n, m, correct_solutions, wrong_solutions):
    correct_solutions.sort()
    wrong_solutions.sort()
    
    min_correct_solution = correct_solutions[0]
    max_correct_solution = correct_solutions[-1]
    
    min_wrong_solution = wrong_solutions[0]
    
    v = min(2*min_correct_solution, max_correct_solution)
    
    if v < min_wrong_solution:
        return v
    else:
        return -1

# Input parsing
n, m = map(int, input().split())
correct_solutions = list(map(int, input().split()))
wrong_solutions = list(map(int, input().split()))

# Call the function and print the result
result = find_minimum_tl(n, m, correct_solutions, wrong_solutions)
print(result)
