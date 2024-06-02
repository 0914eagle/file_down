
def solve_atcode_problem(D, G, problems):
    min_problems = float('inf')
    
    for i in range(2 ** D):
        solved_problems = set()
        total_score = 0
        num_problems = 0
        
        for j in range(D):
            if (i >> j) & 1:
                solved_problems.add(j)
                total_score += 100 * (j + 1) * problems[j][0] + problems[j][1]
                num_problems += problems[j][0]
        
        if total_score >= G:
            min_problems = min(min_problems, num_problems)
        else:
            remaining_problems = set(range(D)) - solved_problems
            max_problem = max(remaining_problems)
            for k in range(problems[max_problem][0]):
                if total_score >= G:
                    break
                total_score += 100 * (max_problem + 1)
                num_problems += 1
        
            if total_score >= G:
                min_problems = min(min_problems, num_problems)
    
    return min_problems

# Input parsing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function and print the result
print(solve_atcode_problem(D, G, problems))
