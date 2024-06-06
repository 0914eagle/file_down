
# https://github.com/TheAlgorithms/Python
# https://github.com/TheAlgorithms/Python/blob/master/project_euler/problem_052/sol1.py
# https://www.geeksforgeeks.org/python-program-to-reverse-a-number/
# https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-or-not/
def isPalindrome(num):
    return str(num) == str(num)[::-1]
 
def getNumber(num):
    num1 = num // 10
    num2 = num % 10
    return 10 * num2 + num1
 
def check():
    num = 0
    for i in range(1000, 10000):
        if isPalindrome(i):
            num = getNumber(i)
            if isPalindrome(num):
                return num
 
print(check())
