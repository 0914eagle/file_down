
def sort_phone_numbers(phone_numbers):
    return sorted(phone_numbers, key=lambda x: int(x.replace("+91", "").replace("91", "").replace("0", "")))

def solve(phone_numbers):
    for phone_number in sort_phone_numbers(phone_numbers):
        print(phone_number)

