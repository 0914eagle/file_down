
def closest(a, b, n):
    return min(abs(a-b), n-abs(a-b))

def solve(n, papers):
    result = set()
    for i in range(n):
        if papers.count(papers[i]) == 1:
            result.add(papers[i])
    return result

n = int(input())
papers = list(map(int, input().split()))
result = solve(n, papers)
if len(result) == 0:
    print("none")
else:
    for x in sorted(result):
        print(x)

