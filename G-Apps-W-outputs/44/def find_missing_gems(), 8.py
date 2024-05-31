
def find_missing_gems():
    gems_dict = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    all_gems = set(["Power", "Time", "Space", "Soul", "Reality", "Mind"])

    n = int(input())
    seen_gems = set()
    for _ in range(n):
        color = input()
        gem_name = gems_dict[color]
        seen_gems.add(gem_name)

    missing_gems = all_gems - seen_gems

    print(len(missing_gems))
    for gem in missing_gems:
        print(gem)

find_missing_gems()
