
def average_grade(N, T, subjects):
    def grade(t, ai, bi, ci):
        return ai * t**2 + bi * t + ci

    def calc_total_grade(time_list):
        total_grade = 0
        for i in range(N):
            total_grade += grade(time_list[i], subjects[i][0], subjects[i][1], subjects[i][2])
        return total_grade / N

    def binary_search():
        epsilon = 1e-6
        left, right = 0, 100

        while right - left > epsilon:
            mid = (left + right) / 2
            time_list = [min(T, mid / subjects[i][0]) for i in range(N)]
            if sum(time_list) <= T:
                left = mid
            else:
                right = mid

        return calc_total_grade(time_list)

    return binary_search()

# Input parsing
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    ai, bi, ci = map(float, input().split())
    subjects.append((ai, bi, ci))

# Calculate and output the maximum average grade
print("{:.10f}".format(average_grade(N, T, subjects)))
