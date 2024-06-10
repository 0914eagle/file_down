
import sys
import re
def golorp(name):
    name = re.sub("[^_\-+\*/:?<>,]", "", name)
    jaws = re.findall("(\?.*\:-)", name)
    if not jaws:
        return "false"
    if not jaws[0][1:-2]:
        return "false"
    diet = re.findall("(_+)", jaws[0][1:-2])
    if not diet:
        return "false"
    if diet[0][0] != "_":
        return "false"
    diet = diet[0][1:]
    num_variables = len(diet)
    variable_values = []
    for i in range(10 ** num_variables):
        value = str(i).zfill(num_variables)
        if eval(re.sub("_", value, diet)) == 0:
            variable_values.append(value)
    if not variable_values:
        return "false"
    return sorted(variable_values)[0]

if __name__ == "__main__":
    name = sys.stdin.read().strip()
    print(golorp(name))

