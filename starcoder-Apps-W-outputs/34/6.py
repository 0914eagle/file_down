
# 1
# 2
# 3

n = int(input())
examples = []
tests = []
for _ in range(n):
    filename, is_example = input().split()
    is_example = int(is_example)
    if is_example:
        examples.append(filename)
    else:
        tests.append(filename)
print(len(examples)+len(tests))
for filename in tests:
    print(f"move {filename} {len(examples)+1}")
    examples.append(filename)
for filename in examples:
    print(f"move {filename} {examples.index(filename)+1}")
