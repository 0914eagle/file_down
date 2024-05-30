
def acronym(s1, s2, s3):
    return ''.join(map(lambda x: x.upper(), filter(lambda x: x != ' ', s1 + s2 + s3)))

if __name__ == '__main__':
    s1, s2, s3 = input().split()
    print(acronym(s1, s2, s3))

