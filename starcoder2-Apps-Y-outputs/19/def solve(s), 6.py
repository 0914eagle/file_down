
def solve(s):
    return s.count('+') - s.count('-')

if __name__ == '__main__':
    s = input()
    print(solve(s))

