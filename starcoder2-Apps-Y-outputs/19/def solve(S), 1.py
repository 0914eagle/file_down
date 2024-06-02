
def solve(S):
    return S.count('+') - S.count('-')

if __name__ == '__main__':
    S = input()
    print(solve(S))

