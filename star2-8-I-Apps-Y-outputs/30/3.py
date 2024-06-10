
import re
from itertools import permutations

def find_golorp_food(golorp):
    jaw_pattern = r"(\d)"
    jaw_values = re.findall(jaw_pattern, golorp)
    num_jaws = len(jaw_values)
    possible_food = set()
    for i in range(num_jaws):
        possible_food.update(permutations(range(10), i))
    possible_food = sorted(possible_food)
    for food in possible_food:
        if evaluate_golorp(golorp, food):
            return "".join(str(v) for v in food)

    return "false"

def evaluate_golorp(golorp, food):
    for i, c in enumerate(golorp):
        if c.isdigit():
            golorp = golorp.replace(c, str(food[i]), 1)
    try:
        result = eval(golorp)
        return result
    except:
        return False

def main():
    golorp = input()
    food = find_golorp_food(golorp)
    print(food)

if __name__ == "__main__":
    main()

