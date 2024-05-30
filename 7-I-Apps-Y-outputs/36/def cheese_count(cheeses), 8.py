
def cheese_count(cheeses):
    soft_cheese = set()
    hard_cheese = set()
    for cheese in cheeses:
        if cheese[1] == "soft":
            soft_cheese.add(cheese[0])
        else:
            hard_cheese.add(cheese[0])
    return len(soft_cheese & hard_cheese)

