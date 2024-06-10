
import re
pattern = r"^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
def is_roman(s):
    return bool(re.match(pattern, s))
if __name__ == '__main__':
    print(is_roman(input()))

