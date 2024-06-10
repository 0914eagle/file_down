
def AmericanFootball(yards):
    total = 0
    for yard in yards:
        total += yard
    
    if total >= 80:
        return "Touchdown"
    
    if total <= -20:
        return "Safety"
    
    return "Nothing"

