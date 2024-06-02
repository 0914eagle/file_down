
def min_steps_to_palindrome(input_num):
    num = str(input_num)
    n = len(num)
    steps = 0
    for i in range(n // 2):
        diff = abs(int(num[i]) - int(num[n - i - 1]))
        steps += min(diff, 10 - diff)
    return steps

# Input
input_num = input().strip()

# Output
print(min_steps_to_palindrome(input_num))
