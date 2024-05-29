
def solve_exam_score(N, K, M, scores):
    current_sum = sum(scores)
    remaining_subjects = N - 1
    remaining_avg = M * N - current_sum

    if remaining_avg > K:
        return -1

    required_score = max(0, remaining_avg)
    return required_score

# Input processing
input_data = input().split()
N, K, M = map(int, input_data[:3])
scores = list(map(int, input_data[3:]))

# Call the function with the calculated values
result = solve_exam_score(N, K, M, scores)
print(result)
