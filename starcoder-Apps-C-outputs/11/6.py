
def time_clock(h, m, s, t_1, t_2):
    # print(h, m, s, t_1, t_2)
    hh = h * 5 + m / 12
    if hh == t_1:
        return True
    elif hh == t_2:
        return False
    elif t_1 < t_2:
        if t_1 <= hh < t_2:
            return False
    else:
        if t_2 <= hh < t_1:
            return True

if __name__ == '__main__':
    h, m, s, t_1, t_2 = list(map(int, input().split()))
    print('YES' if time_clock(h, m, s, t_1, t_2) else 'NO')

