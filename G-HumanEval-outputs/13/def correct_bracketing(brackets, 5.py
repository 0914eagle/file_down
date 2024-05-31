
def correct_bracketing(brackets: str):
    count = 0
    for char in brackets:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0

print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
