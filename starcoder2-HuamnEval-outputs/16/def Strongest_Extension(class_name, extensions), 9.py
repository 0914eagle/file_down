
def Strongest_Extension(class_name, extensions):
    return class_name + '.' + max(extensions, key=lambda x: x.count('A') - x.count('a'))
 