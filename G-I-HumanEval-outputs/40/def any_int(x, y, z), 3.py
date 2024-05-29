
def any_int(x, y, z):
    if all(isinstance(num, int) for num in [x, y, z]):
        if x == y + z or y == x + z or z == x + y:
            return True
    return False

print(any_int(5, 2, 7))  # ➞ True
print(any_int(3, 2, 2))  # ➞ False
print(any_int(3, -2, 1))  # ➞ True
print(any_int(3.6, -2.2, 2))  # ➞ False
