
def solve_atcode_problem(D, G, problems):
    min_problems = float('inf')
    
    for i in range(2**D):
        solved_problems = set()
        total_score = 0
        num_problems = 0
        
        for j in range(D):
            if (i >> j) & 1:
                num_problems += problems[j][0]
                total_score += 100 * (j + 1) * problems[j][0] + problems[j][1]
                solved_problems.add(j)
        
        if total_score >= G:
            min_problems = min(min_problems, num_problems)
        else:
            remaining_problems = set(range(D)) - solved_problems
            max_problem = max(remaining_problems)
            remaining_score = G - total_score
            num_additional_problems = -(-(remaining_score // (100 * (max_problem + 1))) // 1)
            min_problems = min(min_problems, num_problems + num_additional_problems)
    
    return min_problems

# Input processing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function with the input values
result = solve_atcode_problem(D, G, problems)
print(result)
