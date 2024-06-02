
def calculate_tax(bands, percentages, above_band_percentage, friends):
    def calculate_tax_for_band(income, band):
        return (income - band[0]) * band[1] / 100 if income > band[0] else 0

    def calculate_total_tax(income):
        total_tax = 0
        for i in range(bands):
            total_tax += calculate_tax_for_band(income, percentages[i])
        total_tax += (income - percentages[-1][0]) * above_band_percentage / 100
        return total_tax

    def find_income_to_meet_target(target_amount, initial_guess=0):
        left = initial_guess
        right = target_amount
        while right - left > 1e-6:
            mid = (left + right) / 2
            if calculate_total_tax(mid) > target_amount:
                right = mid
            else:
                left = mid
        return left

    results = []
    for friend in friends:
        earned, target_amount = friend
        initial_guess = min(earned, target_amount)
        result = find_income_to_meet_target(target_amount, initial_guess)
        results.append(result)

    return results

# Input parsing
bands = int(input())
percentages = [list(map(float, input().split())) for _ in range(bands)]
above_band_percentage = float(input())
friends_count = int(input())
friends = [list(map(float, input().split())) for _ in range(friends_count)]

# Calculate and output the results
results = calculate_tax(bands, percentages, above_band_percentage, friends)
for result in results:
    print("{:.6f}".format(result))
