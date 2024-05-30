
def acronym(s1, s2, s3):
    return "".join([x[0] for x in [s1, s2, s3] if x.strip()])

print(acronym(input(), input(), input()))

