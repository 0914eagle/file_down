
def is_quasi_palindrome(number):
    number_str = str(number)
    reversed_number_str = number_str[::-1]
    if number_str == reversed_number_str:
        return "YES"
    else:
        return "NO"

number = int(input())
print(is_quasi_palindrome(number))

