
def min_problems_to_solve(D, G, problems):
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
            solve = min(problems[rest_max][0], -(-(G - total_score) // (100 * (rest_max + 1))))
            solved_problems += solve
            total_score += 100 * (rest_max + 1) * solve

        if total_score >= G:
            min_problems = min(min_problems, solved_problems)

    return min_problems

# Input processing
D, G = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(D)]

# Output
print(min_problems_to_solve(D, G, problems))
