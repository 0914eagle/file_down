
def sort_mobile_numbers(l):
    l = [x.strip() for x in l]
    l = sorted(l)
    return l

def print_mobile_numbers(l):
    for x in l:
        print('+91 ' + x[2:5] + ' ' + x[5:])

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        l.append(input())
    l = sort_mobile_numbers(l)
    print_mobile_numbers(l)

