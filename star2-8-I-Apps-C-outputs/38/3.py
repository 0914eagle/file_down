
def find_match(bracket_string, start_index):
open_brackets = 0
for i in range(start_index, len(bracket_string)):
if bracket_string[i] == '(':
open_brackets += 1
elif bracket_string[i] == ')':
open_brackets -= 1
if open_brackets == 0:
return i
return -1

def convert_to_alternative_notation(bracket_string):
headers = []
for i in range(len(bracket_string)):
if bracket_string[i] == '(':
match_index = find_match(bracket_string, i + 1)
if match_index != -1:
headers.append((i + 1, match_index + 1))
i = match_index
alternative_notation = ''
for i, header in enumerate(headers):
start, end = header
if i > 0:
alternative_notation += ':'
alternative_notation += '{},{}:{}'.format(start, end, end)
return alternative_notation

def main():
bracket_string = input()
print(convert_to_alternative_notation(bracket_string))

if __name__ == '__main__':
main()

