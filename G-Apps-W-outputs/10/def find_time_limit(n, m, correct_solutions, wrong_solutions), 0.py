
def find_time_limit(n, m, correct_solutions, wrong_solutions):
    correct_solutions.sort()
    wrong_solutions.sort()
    
    for v in range(correct_solutions[-1], wrong_solutions[0]):
        if all(a <= v and 2*a <= v for a in correct_solutions) and all(b > v for b in wrong_solutions):
            return v
    
    return -1

# Input
n, m = map(int, input().split())
correct_solutions = list(map(int, input().split()))
wrong_solutions = list(map(int, input().split()))

# Output
result = find_time_limit(n, m, correct_solutions, wrong_solutions)
print(result)
