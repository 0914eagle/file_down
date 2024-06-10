
n = int(input())
a = list(map(int, input().split()))

last_seen = dict()
max_len = 0
max_cafe = 0
for i, cafe in enumerate(a):
  if cafe in last_seen:
    if i - last_seen[cafe] > max_len:
      max_len = i - last_seen[cafe]
      max_cafe = cafe
  else:
    last_seen[cafe] = i
    
print(max_cafe)

