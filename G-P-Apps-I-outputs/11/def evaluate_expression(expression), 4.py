
variables = {}

def evaluate_expression(expression):
    if expression.startswith("`"):
        stack = []
        parts = expression.split("${")
        result = ""
        for part in parts:
            if "`" in part:
                stack.append("`" + part)
            else:
                if "}" in part:
                    inner_expr = part.split("}")[0]
                    inner_res = evaluate_expression(inner_expr)
                    stack.append(inner_res + part.split("}")[1])
                else:
                    stack.append(part)
        
        result = "".join(stack)

    elif expression.startswith('"'):
        result = expression[1:-1]

    else:
        result = variables.get(expression)

    return result

while True:
    line = input().strip()
    if line == "end.":
        break

    if line.startswith("var"):
        name, value = line.split(" = ")
        value = value[:-1] if value.endswith(";") else value
        variables[name.split()[1]] = evaluate_expression(value)

    elif line.startswith("print"):
        expr = line.split("print ")[1][:-1]
        print(evaluate_expression(expr))
```
