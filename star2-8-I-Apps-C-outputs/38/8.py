
def find_bracket_pairs(s):
  stack = []
  brackets = []
  for i, c in enumerate(s):
    if c == '(':
      stack.append(i)
    elif c == ')':
      start = stack.pop()
      end = i
      brackets.append((start, end))
  return brackets

def generate_header(start, end):
  return f'{start},{end}:{end},{end}:'

def generate_alternative_bracket_notation(s):
  brackets = find_bracket_pairs(s)
  headers = [generate_header(start, end) for start, end in brackets]
  return ''.join(headers)

s = input()
print(generate_alternative_bracket_notation(s))

