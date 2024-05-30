
def cheese_counter(cheeses):
    soft = 0
    hard = 0
    for cheese in cheeses:
        if cheese[1] == "soft":
            soft += 1
        else:
            hard += 1
    return soft, hard

