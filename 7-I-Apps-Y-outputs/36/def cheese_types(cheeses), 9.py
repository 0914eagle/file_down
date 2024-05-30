
def cheese_types(cheeses):
    types = set()
    for cheese in cheeses:
        types.add(cheese[1])
    return len(types)

