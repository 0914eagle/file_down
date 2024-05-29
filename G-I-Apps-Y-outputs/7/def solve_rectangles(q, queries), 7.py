
def solve_rectangles(q, queries):
    answers = []
    
    for i in range(q):
        n = queries[i][0]
        sticks = queries[i][1]
        
        sticks.sort()
        
        areas = []
        for j in range(2*n):
            if sticks[j] != sticks[4*n-1-j] or sticks[j] * sticks[4*n-1-j] != sticks[j+1] * sticks[4*n-2-j]:
                answers.append("NO")
                break
            if j % 2 == 1:
                areas.append(sticks[j] * sticks[4*n-1-j])
        
        if len(set(areas)) == 1:
            answers.append("YES")
    
    return answers

# Input
q = 5
queries = [
    (1, [1, 1, 10, 10]),
    (2, [10, 5, 2, 10, 1, 1, 2, 5]),
    (2, [10, 5, 1, 10, 5, 1, 1, 1]),
    (2, [1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [10000, 10000, 10000, 10000])
]

# Output
answers = solve_rectangles(q, queries)
for ans in answers:
    print(ans)
