
def solve(s):
    return min(s.count('B'), s.count('W'))

if __name__ == '__main__':
    s = input()
    print(solve(s))

