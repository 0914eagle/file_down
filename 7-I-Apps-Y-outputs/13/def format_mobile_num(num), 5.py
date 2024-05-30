
def format_mobile_num(num):
    return "+91 " + " ".join(num[2:])

def sort_mobile_num(num):
    return sorted(num, key=lambda x: int(x[2:]))

def mobile_nums(nums):
    return map(format_mobile_num, sort_mobile_num(nums))

