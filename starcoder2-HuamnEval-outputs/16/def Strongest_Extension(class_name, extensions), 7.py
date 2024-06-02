
 def Strongest_Extension(class_name, extensions):
    return '{}.{}'.format(class_name, max(extensions, key=lambda x: len([i for i in x if i.isupper()]) - len([i for i in x if i.islower()])))
 