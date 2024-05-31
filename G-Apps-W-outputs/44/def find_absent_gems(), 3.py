
def find_absent_gems():
    gems_colors = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    gems_present = set()
    for _ in range(int(input())):
        gems_present.add(gems_colors[input()])

    gems_absent = set(gems_colors.values()) - gems_present

    print(len(gems_absent))
    for gem in gems_absent:
        print(gem)

find_absent_gems()
