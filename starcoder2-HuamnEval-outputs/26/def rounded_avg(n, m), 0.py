
 def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        return bin(round((m - n + 1) / 2 + n))
