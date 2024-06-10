
from sys import stdin
from collections import defaultdict
from math import factorial
def binom(n, k):
  return factorial(n) // (factorial(k) * factorial(n - k))
def prob(n, k):
  return 1 / binom(n, k)
n = int(stdin.readline().rstrip())
l = int(stdin.readline().rstrip())
walk = [int(x) for x in stdin.readline().rstrip().split()]
graph = defaultdict(list)
for i in range(n):
  line = [int(x) for x in stdin.readline().rstrip().split()]
  graph[i] = line[1:]
def dfs(node):
  if len(graph[node]) == 0:
    return 1
  s = 0
  for n in graph[node]:
    s += dfs(n)
  return s
def prob_node(node):
  return 1 / dfs(node)
def prob_edge(u, v):
  if u == v:
    return 1
  return (1 / dfs(u)) * (1 / (len(graph[u]) - 1))
ans = 1
for i in range(l):
  ans *= prob_node(walk[i])
for i in range(l - 1):
  ans *= prob_edge(walk[i], walk[i + 1])
print(ans)

