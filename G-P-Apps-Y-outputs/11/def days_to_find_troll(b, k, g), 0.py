
def days_to_find_troll(b, k, g):
    if k <= g:
        return 1
    else:
        days = 0
        while k > 0:
            k -= g
            days += 1
        return days

# Input
input_str = input().strip()
b, k, g = map(int, input_str.split())

# Output
print(days_to_find_troll(b, k, g))
