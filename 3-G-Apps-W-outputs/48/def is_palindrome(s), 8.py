
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
    current_time_str = f"{hh:02d}:{mm:02d}"
    
    if is_palindrome(current_time_str):
        return 0
    
    next_palindrome_time = find_next_palindrome_time(current_time)
    
    next_hh, next_mm = map(int, next_palindrome_time.split(':'))
    
    minutes_diff = (next_hh - hh) * 60 + (next_mm - mm)
    
    if minutes_diff < 0:
        minutes_diff += 24 * 60
    
    return minutes_diff

# Input
current_time = input().strip()

# Output
print(minutes_to_next_palindrome(current_time))
