
def solve(s):
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            for j in range(i, n, i+1):
                s[j] = '1' if s[j] == '0' else '0'
    return s.count('1') == n

def main():
    s = input()
    print(solve(list(s)))

if __name__ == '__main__':
    main()

