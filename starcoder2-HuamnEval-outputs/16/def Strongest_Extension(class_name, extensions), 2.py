
 def Strongest_Extension(class_name, extensions):
    return '{}.{}'.format(class_name, max(extensions, key=lambda x: len([c for c in x if c.isupper()]) - len([c for c in x if c.islower()])))
