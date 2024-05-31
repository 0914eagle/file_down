
def check_if_palindrome(input_string):
    reversed_string = input_string[::-1]
    if input_string == reversed_string:
        return "YES"
    else:
        return "NO"

# Test cases
test_cases = ["GENIUS", "DOCTOR", "IRENE", "MARY", "SMARTPHONE", "REVOLVER", "HOLMES", "WATSON"]
for test_case in test_cases:
    print(check_if_palindrome(test_case))
