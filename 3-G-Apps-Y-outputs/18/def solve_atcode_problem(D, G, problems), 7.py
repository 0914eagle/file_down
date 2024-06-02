
def solve_atcode_problem(D, G, problems):
    min_problems = float('inf')
    
    for mask in range(1 << D):
        solved = 0
        score = 0
        bonus = 0
        
        for i in range(D):
            if mask & (1 << i):
                solved += problems[i][0]
                score += problems[i][0] * 100 * (i + 1) + problems[i][1]
                bonus += problems[i][0]
        
        if score >= G:
            min_problems = min(min_problems, solved)
        else:
            for i in range(D - 1, -1, -1):
                if not mask & (1 << i):
                    remaining = G - score
                    extra_problems = (remaining + 100 * (i + 1) - 1) // (100 * (i + 1))
                    if extra_problems >= problems[i][0]:
                        continue
                    solved += extra_problems
                    min_problems = min(min_problems, solved)
                    break
    
    return min_problems

# Input parsing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function and print the result
print(solve_atcode_problem(D, G, problems))
