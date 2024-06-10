
def solve(f, s, g, u, d):
    if (s == g):
        return 0
    if (u == 0):
        if (s > g):
            return (s - g) // d
        return "use the stairs"
    if (d == 0):
        if (s < g):
            return (g - s) // u
        return "use the stairs"
    if (s > g):
        return (s - g) // d + (s - g) % d
    return (g - s) // u + (g - s) % u

