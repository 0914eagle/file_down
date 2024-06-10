
def guessing_circle(n, papers):
    freq = {}
    for paper in papers:
        freq[paper] = freq.get(paper, 0) + 1
    
    result = []
    for paper in papers:
        if freq[paper] == 1:
            result.append(paper)
    
    if len(result) == 0:
        print("none")
    else:
        for x in sorted(result):
            print(x)

n = int(input())
papers = list(map(int, input().split()))
guessing_circle(n, papers)

