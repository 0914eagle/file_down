
import re

def is_valid_golorp(name):
    name = name.replace('?', '')
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace('<', '')
    name = name.replace('>', '')
    name = name.replace(',', '')
    name = name.replace('.', '')
    name = name.replace('_', '')
    name = name.replace(':', '')
    name = name.replace('*', '')
    name = name.replace('+', '')
    name = name.replace('-', '')
    name = name.replace('/', '')
    if len(name) > 0:
        return False
    return True


def solve_golorp(name):
    if not is_valid_golorp(name):
        return "false"
    
    jaws_pattern = r"\?(\(([^)]+)\))"
    jaws_matches = re.findall(jaws_pattern, name)
    
    stomach_pattern = r"\?(\(([^)]+)\),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^)]+))"
    stomach_matches = re.findall(stomach_pattern, name)
    
    if len(jaws_matches) != len(stomach_matches):
        return "false"
    
    for i in range(len(jaws_matches)):
        jaws_variables = jaws_matches[i][1].split('_')
        stomach_variables = stomach_matches[i][1].split('_')
        if len(jaws_variables) != len(stomach_variables):
            return "false"
    
    return "0" * len(jaws_matches)

if __name__ == "__main__":
    name = input()
    print(solve_golorp(name))

