
def steps_to_palindrome(counter):
    counter = str(counter)
    n = len(counter)
    steps = 0
    for i in range(n // 2):
        diff = abs(int(counter[i]) - int(counter[n - i - 1]))
        steps += min(diff, 10 - diff)
    return steps

# Read input
counter = input().strip()

# Calculate and print the minimum number of steps to reach a palindrome
print(steps_to_palindrome(counter))
