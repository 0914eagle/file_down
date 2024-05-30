
def sort_mobile(l):
    return sorted(l, key=lambda x: int(x[3:]))

def format_mobile(l):
    return ['+91 {} {}'.format(x[:5], x[5:]) for x in l]

def mobile_sort(l):
    return format_mobile(sort_mobile(l))

def mobile_sort(l):
    return format_mobile(sort_mobile(l))


