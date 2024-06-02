
def steps_to_palindrome(input_num):
    def is_palindrome(num_str):
        return num_str == num_str[::-1]

    steps = 0
    while not is_palindrome(input_num):
        input_num = str(int(input_num) + 1)
        steps += 1

    return steps

# Read input
input_num = input().strip()

# Output result
print(steps_to_palindrome(input_num))
