
def Strongest_Extension(class_name, extensions):
    return '{}.{}'.format(class_name, max(extensions, key=lambda x: sum(c.isupper() for c in x) - sum(c.islower() for c in x)))
