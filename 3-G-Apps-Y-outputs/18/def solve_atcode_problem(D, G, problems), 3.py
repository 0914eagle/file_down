
def solve_atcode_problem(D, G, problems):
    min_problems = float('inf')
    
    for mask in range(1 << D):
        solved_problems = 0
        total_score = 0
        bonus_score = 0
        
        for i in range(D):
            if mask & (1 << i):
                solved_problems += problems[i][0]
                total_score += problems[i][0] * 100 * (i + 1) + problems[i][1]
                bonus_score += problems[i][1]
        
        if total_score >= G:
            min_problems = min(min_problems, solved_problems)
        else:
            remaining = G - total_score
            for i in range(D - 1, -1, -1):
                if mask & (1 << i):
                    continue
                num_problems_needed = (remaining + 100 * (i + 1) - 1) // (100 * (i + 1))
                if num_problems_needed >= problems[i][0]:
                    continue
                solved_problems += num_problems_needed
                min_problems = min(min_problems, solved_problems)
                break
    
    return min_problems

# Input processing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function and print the result
print(solve_atcode_problem(D, G, problems))
