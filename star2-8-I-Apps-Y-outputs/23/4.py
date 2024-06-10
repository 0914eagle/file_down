
def process_query(query):
  if query[0] == 1:
    s[query[1] - 1] = query[2]
  else:
    chars = set()
    for i in range(query[1] - 1, query[2]):
      chars.add(s[i])
    return len(chars)

s = input()
q = int(input())
for i in range(q):
  query = list(map(int, input().split()))
  if query[0] == 2:
    print(process_query(query))
  else:
    process_query(query)

