
def below_threshold(l: list, t: int):
    return all(x < t for x in l)

print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))  # False
