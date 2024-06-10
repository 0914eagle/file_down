
def solve(n, papers):
    counts = {}
    for x in papers:
        counts[x] = counts.get(x, 0) + 1
    
    result = []
    for x in counts:
        if counts[x] == 1:
            result.append(x)
    
    result.sort()
    
    if len(result) == 0:
        print("none")
    else:
        print("\n".join(map(str, result)))

n = int(input())
papers = list(map(int, input().split()))
solve(n, papers)

