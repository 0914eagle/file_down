
def find_absent_gems():
    gems_dict = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    n = int(input())
    seen_gems = [input() for _ in range(n)]

    absent_gems = []
    for color, gem_name in gems_dict.items():
        if color not in seen_gems:
            absent_gems.append(gem_name)

    print(len(absent_gems))
    for gem in absent_gems:
        print(gem)

find_absent_gems()
