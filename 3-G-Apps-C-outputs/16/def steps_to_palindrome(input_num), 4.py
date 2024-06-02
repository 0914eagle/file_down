
def steps_to_palindrome(input_num):
    num = str(input_num)
    length = len(num)
    steps = 0
    for i in range(length // 2):
        diff = abs(int(num[i]) - int(num[length - i - 1]))
        steps += min(diff, 10 - diff)
    return steps

# Read input
input_num = input().strip()

# Call the function and print the output
print(steps_to_palindrome(input_num))
