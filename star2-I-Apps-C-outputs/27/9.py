
from collections import defaultdict

def guessing_circle(n, papers):
    counts = defaultdict(int)
    for paper in papers:
        counts[paper] += 1

    result = []
    for paper in papers:
        if counts[paper] == 1:
            result.append(paper)

    if len(result) == 0:
        print("none")
    else:
        print("\n".join(map(str, sorted(result))))

n = int(input())
papers = list(map(int, input().split()))
guessing_circle(n, papers)

