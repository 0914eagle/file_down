
def is_palindrome(s):
    return s == s[::-1]

def next_palindrome_time(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        mm += 1
        if mm == 60:
            mm = 0
            hh = (hh + 1) % 24
        time_str = f"{hh:02d}:{mm:02d}"
        if is_palindrome(time_str):
            return time_str

def minutes_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(':'))
    while True:
        time_str = f"{hh:02d}:{mm:02d}"
        if is_palindrome(time_str):
            return 0
        current_time = next_palindrome_time(time_str)
        hh, mm = map(int, current_time.split(':'))

current_time = input().strip()
print(minutes_to_palindrome(current_time))
