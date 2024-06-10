
import sys
def solve(s):
stack = []
res = []
for i, c in enumerate(s):
if c == '(':
stack.append(i)
else:
start = stack.pop()
end = i + 1
res.append((start, end))
if not stack:
res.sort(key=lambda x: x[0])
start = res[0][0]
end = res[-1][1]
res = [str(x) for x in [start, end]]
return ",".join(res) + ":" * (len(res) - 1)

if __name__ == "__main__":
s = sys.stdin.read().strip()
print(solve(s))

