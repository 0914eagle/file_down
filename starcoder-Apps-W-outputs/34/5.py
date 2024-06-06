
n = int(input())

examples = []
tests = []

for i in range(n):
    x = input().split()
    if x[1] == '1':
        examples.append(x[0])
    else:
        tests.append(x[0])

print(len(examples) + len(tests))

for i in examples:
    print("move {} {}".format(i, len(examples) - examples.index(i)))

for i in tests:
    print("move {} {}".format(i, len(examples) + len(tests) - tests.index(i)))
