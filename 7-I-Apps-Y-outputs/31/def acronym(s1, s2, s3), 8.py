
def acronym(s1, s2, s3):
    return "".join([i[0].upper() for i in [s1, s2, s3]])

s1, s2, s3 = input().split()
print(acronym(s1, s2, s3))

