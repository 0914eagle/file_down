
def format_mobile(mobile):
    if mobile.startswith('+91'):
        return mobile[0:11]
    elif mobile.startswith('91'):
        return mobile[0:11]
    elif mobile.startswith('0'):
        return mobile[0:11]
    else:
        return mobile[0:10]

def sort_mobile(l):
    return sorted(l, key=format_mobile)

def read_input():
    N = int(input())
    l = []
    for i in range(N):
        l.append(input())
    return l

def print_output(l):
    for i in l:
        print('+91 ' + i[2:5] + ' ' + i[5:8] + ' ' + i[8:])

l = read_input()
print_output(sort_mobile(l))

