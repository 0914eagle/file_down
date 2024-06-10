
import re
def feed_golorp(name):
    jaws = re.findall(r"\[([0-9]+)\]", name)
    stomach = re.findall(r"\{([0-9]+)\}", name)
    if len(jaws) != len(stomach):
        return "false"
    values = [0] * len(jaws)
    for i in range(len(jaws)):
        jaw = int(jaws[i])
        stomach_value = int(stomach[i])
        if values[jaw] != 0 and values[jaw] != stomach_value:
            return "false"
        values[jaw] = stomach_value
    return "".join(map(str, values))

name = input()
print(feed_golorp(name))

