
def solve(d, b, f, t0, t1, t2):
    fruits = f
    trees = [t0, t1, t2]
    days_to_harvest = [3, 2, 1]
    for day in range(d):
        b += fruits * 100
        for i in range(len(days_to_harvest)):
            if day % days_to_harvest[i] == 0:
                fruits += trees[i]
        if b >= 400:
            b -= 400
            fruits += 1
    return b


