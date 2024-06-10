
def solve(r, s, p):
    total = r + s + p
    r_prob = r / total
    s_prob = s / total
    p_prob = p / total
    r_prob_next = s_prob * p_prob
    s_prob_next = r_prob * p_prob
    p_prob_next = r_prob * s_prob
    while abs(r_prob - r_prob_next) > 1e-9 or abs(s_prob - s_prob_next) > 1e-9 or abs(p_prob - p_prob_next) > 1e-9:
        r_prob = r_prob_next
        s_prob = s_prob_next
        p_prob = p_prob_next
        r_prob_next = s_prob * p_prob
        s_prob_next = r_prob * p_prob
        p_prob_next = r_prob * s_prob
    return r_prob, s_prob, p_prob

r, s, p = map(int, input().split())
print(*solve(r, s, p))

