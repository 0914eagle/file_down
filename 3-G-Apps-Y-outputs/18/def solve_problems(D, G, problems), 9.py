
def solve_problems(D, G, problems):
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
            for i in range(D - 1, -1, -1):
                if not mask & (1 << i):
                    remaining_problems = problems[i][0]
                    while remaining_problems > 0 and total_score < G:
                        total_score += 100 * (i + 1)
                        bonus_score += 100 * (i + 1)
                        solved_problems += 1
                        remaining_problems -= 1
        
                    if total_score >= G:
                        min_problems = min(min_problems, solved_problems)
                        break
    
    return min_problems

# Input parsing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function with the input values
result = solve_problems(D, G, problems)
print(result)
