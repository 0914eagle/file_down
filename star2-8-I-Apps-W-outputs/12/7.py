
def get_result(yards):
    pos = 20  # starting position
    for yard in yards:
        pos += yard
        if pos >= 80:  # Touchdown
            return "Touchdown"
        elif pos <= 0:  # Safety
            return "Safety"
    return "Nothing"

