
def max_calories(n, m, calories):
    max_calories = 0
    remaining_hours = 0
    for i in range(n):
        if calories[i] <= m:
            max_calories += calories[i]
            m -= calories[i]
            remaining_hours = 0
        else:
            remaining_hours += 1
            if remaining_hours == 2:
                m = max(m, calories[i])
                remaining_hours = 0
    return max_calories

# Input
input_line = input().split()
n = int(input_line[0])
m = int(input_line[1])
calories = list(map(int, input().split()))

# Output
print(max_calories(n, m, calories))
