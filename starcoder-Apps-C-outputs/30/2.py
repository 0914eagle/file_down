
# 20190821

sentence = input()
n = int(input())
d = []
for i in range(n):
    d.append(input())

# 所有排列情况
def get_all_permutations(input_string):
    if len(input_string) <= 1:
        yield input_string
    else:
        for permutation in get_all_permutations(input_string[1:]):
            for i in range(len(permutation) + 1):
                yield permutation[:i] + input_string[0:1] + permutation[i:]

result = []
for x in get_all_permutations(sentence):
    #print(x)
    temp = ""
    count = 0
    for i in range(len(sentence)):
        if x[i] == ' ':
            count += 1
        else:
            temp += x[i]
    if temp in d and count == temp.count(' '):
        result.append(x)

if len(result) == 0:
    print('impossible')
elif len(result) == 1:
    print(result[0])
else:
    print('ambiguous')
