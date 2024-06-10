
def socks(s, c, k, d):
    machines = 1
    socks_in_machine = 1
    for i in range(1, s):
        if abs(d[i] - d[i - 1]) <= k:
            socks_in_machine += 1
        else:
            machines += 1
            socks_in_machine = 1
        if socks_in_machine > c:
            machines += 1
            socks_in_machine = 1
    return machines


