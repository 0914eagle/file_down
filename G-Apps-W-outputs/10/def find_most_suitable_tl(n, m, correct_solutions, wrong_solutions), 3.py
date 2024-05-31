
def find_most_suitable_tl(n, m, correct_solutions, wrong_solutions):
    correct_min = min(correct_solutions)
    correct_max_double = max(correct_solutions) * 2
    wrong_max = max(wrong_solutions)
    
    if correct_max_double < wrong_max and correct_max_double < wrong_max + 1:
        return correct_max_double
    elif correct_max_double < wrong_max and correct_max_double >= wrong_max + 1:
        return -1
    
    for v in range(correct_max_double, wrong_max + 1):
        if all(solution <= v for solution in correct_solutions) and any(solution <= 2*v for solution in correct_solutions) and all(solution > v for solution in wrong_solutions):
            return v
    
    return -1

# Input
n, m = map(int, input().split())
correct_solutions = list(map(int, input().split()))
wrong_solutions = list(map(int, input().split()))

# Output
result = find_most_suitable_tl(n, m, correct_solutions, wrong_solutions)
print(result)
