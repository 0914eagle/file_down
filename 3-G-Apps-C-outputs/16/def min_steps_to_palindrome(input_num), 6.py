
def min_steps_to_palindrome(input_num):
    def is_palindrome(num_str):
        return num_str == num_str[::-1]

    num_steps = 0
    while not is_palindrome(input_num):
        input_num = str(int(input_num) + 1)
        num_steps += 1

    return num_steps

# Read input
input_num = input().strip()

# Call the function and print the output
print(min_steps_to_palindrome(input_num))
