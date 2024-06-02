
def solve_problems(D, G, problems):
    min_problems = float('inf')
    
    for mask in range(1 << D):
        solved_problems = 0
        total_score = 0
        rest_max = -1
        
        for i in range(D):
            if mask & (1 << i):
                solved_problems += problems[i][0]
                total_score += 100 * (i + 1) * problems[i][0] + problems[i][1]
            else:
                rest_max = i
        
        if total_score < G:
            solve_rest = max(0, (G - total_score + 100 * (rest_max + 1) - 1) // (100 * (rest_max + 1)))
            if solve_rest + solved_problems < min_problems:
                min_problems = solve_rest + solved_problems
    
    return min_problems

# Input parsing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Call the function and print the result
print(solve_problems(D, G, problems))
