

def solve(n,m,k,o,c,adj):
  pass

def main():
  n,m,k = map(int,input().split())
  o = list(map(int,input().split()))
  c = list(map(int,input().split()))
  adj = [[] for _ in range(n)]
  for i in range(n):
    a = list(map(int,input().split()))
    for j in range(1,len(a)):
      adj[i].append(a[j])
  print(solve(n,m,k,o,c,adj))

if __name__ == "__main__":
  main()


