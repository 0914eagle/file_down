
def find_absent_gems():
    gems = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    n = int(input())
    present_gems = set()
    
    for _ in range(n):
        color = input()
        present_gems.add(gems[color])

    absent_gems = set(gems.values()) - present_gems

    print(len(absent_gems))
    for gem in absent_gems:
        print(gem)

find_absent_gems()
