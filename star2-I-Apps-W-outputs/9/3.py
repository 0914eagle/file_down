
from sys import stdin

def read_ints():
    return list(map(int, stdin.readline().split()))

def read_strs():
    return list(map(str, stdin.readline().split()))

def read_str():
    return str(stdin.readline().strip())

def read_int():
    return int(stdin.readline())

def main():
    n, m = read_ints()
    t = read_strs()
    s = read_strs()
    t_str = ""
    s_str = ""
    for i in range(n):
        t_str += t[i][2] * int(t[i][0])
    for i in range(m):
        s_str += s[i][2] * int(s[i][0])
    count = 0
    for i in range(len(t_str) - len(s_str) + 1):
        if t_str[i:i+len(s_str)] == s_str:
            count += 1
    print(count)

if __name__ == "__main__":
    main()

