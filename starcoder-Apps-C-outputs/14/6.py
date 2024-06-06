
import re

text = input()

text = re.sub(r'[,?!;.:]', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()

text = text.split(' ')

first = 0
second = 0
third = 0

result = []

for i in range(len(text)):
    if first != 5 and second != 7 and third != 5:
        if first == 5:
            third += 1
            result.append(text[i])
        elif second == 7:
            first += 1
            result.append(text[i])
        else:
            second += 1
            result.append(text[i])
    else:
        break

if first == 5 and second == 7 and third == 5:
    print('\n'.join(result))
else:
    print(text)
