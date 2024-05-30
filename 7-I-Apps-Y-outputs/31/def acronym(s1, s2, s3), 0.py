
def acronym(s1, s2, s3):
    return "".join(map(lambda x: x.upper(), s1.split()[0])) + "".join(map(lambda x: x.upper(), s2.split()[0])) + "".join(map(lambda x: x.upper(), s3.split()[0]))

print(acronym(input(), input(), input()))

