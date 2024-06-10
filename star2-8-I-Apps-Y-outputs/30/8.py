
import re

def check_jaws(jaws, values):
    
    for i, c in enumerate(jaws):
        if c == '_':
            continue
        if c == '+' or c == '-':
            if values[i] == '0':
                values[i] = '1' if c == '+' else '9'
            elif values[i] == '9':
                values[i] = '8' if c == '+' else '0'
            else:
                values[i] = str(int(values[i]) + 1) if c == '+' else str(int(values[i]) - 1)
        elif c == '*' or c == '/':
            if values[i] == '0':
                values[i] = '1' if c == '*' else '0'
            elif values[i] == '1':
                values[i] = '0' if c == '*' else '1'
    return True


def feed_golorp(name):
    
    m = re.match(r'\?(\([^)]*\)):(-*_*_*>*_*_*,)*(-*_*_*>*_*_*,)*', name)
    if not m:
        return 'false'
    jaws = m.group(1)
    num_variables = jaws.count('_')
    num_values = len(name) - len(jaws) - 1
    if num_values < num_variables:
        return 'false'
    jaws_values = [c for c in jaws if c == '_']
    best_values = None
    best_value = None
    for i in range(num_values - num_variables + 1):
        values = list(name[i:i + num_variables])
        if check_jaws(jaws, values):
            value = ''.join(values)
            if not best_value or value < best_value:
                best_value = value
                best_values = values
    return ''.join(best_values) if best_values else 'false'

