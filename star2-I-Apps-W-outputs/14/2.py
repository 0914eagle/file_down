
def solve(r, s, p):
    total = r + s + p
    r_prob = r / total
    s_prob = s / total
    p_prob = p / total
    while True:
        new_r_prob = r_prob * (1 - s_prob)
        new_s_prob = s_prob * (1 - p_prob)
        new_p_prob = p_prob * (1 - r_prob)
        if abs(new_r_prob - r_prob) < 1e-9 and abs(new_s_prob - s_prob) < 1e-9 and abs(new_p_prob - p_prob) < 1e-9:
            break
        r_prob = new_r_prob
        s_prob = new_s_prob
        p_prob = new_p_prob
    return r_prob, s_prob, p_prob


if __name__ == '__main__':
    r, s, p = map(int, input().split())
    r_prob, s_prob, p_prob = solve(r, s, p)
    print(r_prob, s_prob, p_prob)

