
def max_bling(d, b, f, t0, t1, t2):
    if d == 1:
        return b + f*100
    elif d <= 4:
        max_bling = b
        max_bling += min(d-1, t0)*300
        max_bling += min(d-1, t1)*500
        max_bling += min(d-1, t2)*500
        max_bling += min(d-1, f)*100
        return max_bling
    else:
        max_bling = b
        max_bling += t0*300
        max_bling += t1*500
        max_bling += t2*500
        max_bling += f*100
        max_bling += min(d-4, t0+t1+t2+f)*100
        return max_bling

