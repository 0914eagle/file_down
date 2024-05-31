
def calculate_grade(N, T, subjects):
    def calculate_grade_single(subject, t):
        return subject[0] * t**2 + subject[1] * t + subject[2]

    def binary_search(subject, target_grade):
        low, high = 0, T
        eps = 1e-9

        while high - low > eps:
            mid = (high + low) / 2
            if calculate_grade_single(subject, mid) < target_grade:
                low = mid
            else:
                high = mid

        return low

    max_average_grade = 0

    for subject in subjects:
        low_time = binary_search(subject, 0)
        high_time = binary_search(subject, 100)

        for _ in range(1000):
            mid_time = (low_time + high_time) / 2
            grade = calculate_grade_single(subject, mid_time)
            if grade > 100:
                high_time = mid_time
            else:
                low_time = mid_time

        max_average_grade += calculate_grade_single(subject, mid_time) / N

    return max_average_grade

# Reading input
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Calculating and printing the maximum average grade
print("{:.10f}".format(calculate_grade(N, T, subjects)))
