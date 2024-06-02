
def is_palindrome(time_str):
    return time_str == time_str[::-1]

def minutes_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh = (hh + 1) % 24
        if is_palindrome(f"{hh:02d}:{mm:02d}"):
            return (hh - int(current_time[:2])) * 60 + mm - int(current_time[3:])

# Input
current_time = input().strip()

# Output
print(minutes_to_palindrome(current_time))
