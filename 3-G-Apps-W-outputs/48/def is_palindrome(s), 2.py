
def is_palindrome(s):
    return s == s[::-1]

def find_next_palindrome_time(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh = (hh + 1) % 24
        if is_palindrome(f"{hh:02d}:{mm:02d}"):
            return f"{hh:02d}:{mm:02d}"

def minutes_to_next_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        current_time = find_next_palindrome_time(f"{hh:02d}:{mm:02d}")
        hh, mm = map(int, current_time.split(':'))
        if current_time == current_time[::-1]:
            return (hh - int(current_time[:2])) * 60 + mm - int(current_time[3:])

# Input
current_time = input().strip()

# Output
print(minutes_to_next_palindrome(current_time))
