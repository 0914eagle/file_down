
def steps_to_palindrome(num):
    def is_palindrome(s):
        return s == s[::-1]

    steps = 0
    while not is_palindrome(num):
        num = str(int(num) + 1)
        steps += 1

    return steps

# Read input
input_num = input().strip()

# Calculate and print output
print(steps_to_palindrome(input_num))
