
def compare_numbers(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if num1 > num2:
        return num1
    else:
        return num2

num1, num2 = input().split()
print(compare_numbers(num1, num2)[::-1])

