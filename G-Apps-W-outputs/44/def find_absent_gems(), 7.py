
def find_absent_gems():
    gem_colors = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    n = int(input())
    seen_gems = set(input().strip() for _ in range(n))

    all_gems = set(gem_colors.keys())
    absent_gems = all_gems - seen_gems

    print(len(absent_gems))
    for color in absent_gems:
        print(gem_colors[color])

find_absent_gems()
