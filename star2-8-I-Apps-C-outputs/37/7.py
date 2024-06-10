
def max_bling(d, b, f, t0, t1, t2):
    def max_bling_aux(d, b, f, t0, t1, t2):
        if d == 0:
            return b
        exotic = (d >= 4 and b >= 400)
        if exotic:
            b -= 400
            t2 += 1
        return max(max_bling_aux(d - 1, b + 100 * f + 500 * t2, 0, t0 + t2, t1 + t2, 0),
                   max_bling_aux(d - 1, b, f + 1, t0, t1, t2),
                   max_bling_aux(d - 1, b, f, t0, t1, t2))
        
    return max_bling_aux(d, b, f, t0, t1, t2)

