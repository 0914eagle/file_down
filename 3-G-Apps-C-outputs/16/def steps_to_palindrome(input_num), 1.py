
def steps_to_palindrome(input_num):
    num = str(input_num)
    n = len(num)
    steps = 0
    for i in range(n//2):
        diff = abs(int(num[i]) - int(num[n-1-i]))
        steps += min(diff, 10 - diff)
    return steps

# Read input
input_num = input().strip()

# Calculate and print the minimum number of steps to reach a palindrome
print(steps_to_palindrome(input_num))
