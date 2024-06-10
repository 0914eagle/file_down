
def is_balanced(s):
  stack = []
  for c in s:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if len(stack) == 0 or stack[-1] != "(":
        return False
      else:
        stack.pop()
  return len(stack) == 0

def convert_to_alternative_bracket_notation(s):
  if not is_balanced(s):
    raise ValueError("Input string is not balanced")
  open_brackets = []
  for i, c in enumerate(s):
    if c == "(":
      open_brackets.append(i)
    elif c == ")":
      start = open_brackets.pop()
      end = i
      subsequence = s[start+1:end]
      header = f"{start},{end}:"
      s = s.replace(f"({subsequence})", header)
  return s

s = input()
print(convert_to_alternative_bracket_notation(s))

