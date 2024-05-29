
def is_lucky_number(a):
    # Check if the number is divisible by both 2 and 3
    if a % 2 == 0 and a % 3 == 0:
        return 1
    else:
        return 0

# Read input
a = int(input().strip())

result = is_lucky_number(a)
print(result)
