
def eat(number, need, remaining):
    total_carrots = number + need
    if remaining >= need:
        remaining_carrots = remaining - need
    else:
        remaining_carrots = 0
    return [total_carrots, remaining_carrots]
