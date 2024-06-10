
def minimumDistance(current, correct):
    diff = abs(current - correct)
    if diff > 180:
        diff = 360 - diff
    if current > correct:
        diff = -diff
    return diff

