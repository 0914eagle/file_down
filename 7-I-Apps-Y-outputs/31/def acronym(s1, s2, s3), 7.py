
def acronym(s1, s2, s3):
    return ''.join(map(lambda x: x[0].upper(), (s1, s2, s3)))

print(acronym(input(), input(), input()))

