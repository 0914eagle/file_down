
def compare(num1, num2):
    return str(max(num1, num2))[::-1]

num1, num2 = list(map(int, input().split()))
print(compare(num1, num2))

