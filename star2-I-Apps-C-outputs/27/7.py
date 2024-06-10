
def guessing_circle(n, papers):
    counts = [0] * 15001
    for paper in papers:
        counts[paper] += 1
    
    result = []
    for i in range(1, 15001):
        if counts[i] == 1:
            result.append(i)
    
    if len(result) == 0:
        print("none")
    else:
        print("\n".join(map(str, result)))

n = int(input())
papers = list(map(int, input().split()))
guessing_circle(n, papers)

