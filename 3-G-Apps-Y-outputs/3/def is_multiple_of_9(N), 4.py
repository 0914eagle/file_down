
def is_multiple_of_9(N):
    digit_sum = sum(int(digit) for digit in str(N))
    if digit_sum % 9 == 0:
        return "Yes"
    else:
        return "No"

N = int(input())
print(is_multiple_of_9(N))
