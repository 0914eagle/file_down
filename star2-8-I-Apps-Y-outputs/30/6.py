
import sys
import re

def feed(name):
    pattern = r"\?(\([^()]+\)):(-[^()]+)\."
    match = re.match(pattern, name)
    if match is None:
        return "false"
    
    jaws, stomach = match.groups()
    jaws = jaws[1:-1]
    stomach = stomach[1:-1]
    
    jaw_pattern = r"(\_+)|(\*+)|(\++)|(-+)"
    jaw_parts = re.findall(jaw_pattern, jaws)
    
    result = []
    
    for part in jaw_parts:
        for symbol in part:
            if symbol != "":
                value = ord(symbol) - ord("_")
                if symbol == "*":
                    result.append(str(value))
                else:
                    result.append(str(value) * value)
    
    return "".join(result)

def main():
    name = sys.stdin.readline().strip()
    
    print(feed(name))

if __name__ == "__main__":
    main()

