
def min_steps_to_palindrome(counter):
    counter = str(counter)
    n = len(counter)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    if is_palindrome(counter):
        return 0
    
    steps = 0
    for i in range(n // 2):
        diff = abs(int(counter[i]) - int(counter[n - i - 1]))
        steps += min(diff, 10 - diff)
    
    return steps

# Input
counter = input().strip()

# Output
print(min_steps_to_palindrome(counter))
